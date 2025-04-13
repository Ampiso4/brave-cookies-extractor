import sqlite3
import json
import os
import argparse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_brave_cookies(url):
    """Extract cookies from Brave's SQLite database"""
    brave_path = os.path.expanduser('~/.config/BraveSoftware/Brave-Browser/Default')
    cookies_db = os.path.join(brave_path, 'Cookies')
    
    if not os.path.exists(cookies_db):
        raise FileNotFoundError("Brave cookies database not found")
    
    conn = sqlite3.connect(cookies_db)
    cursor = conn.cursor()
    
    domain = url.split('//')[-1].split('/')[0]
    query = """
        SELECT name, value, host_key, path, expires_utc, is_secure, is_httponly 
        FROM cookies 
        WHERE host_key LIKE ? OR host_key LIKE ?
    """
    cursor.execute(query, (f"%{domain}", f".{domain}"))
    
    cookies = []
    for row in cursor.fetchall():
        cookies.append({
            'name': row[0],
            'value': row[1],
            'domain': row[2],
            'path': row[3],
            'expires': row[4],
            'secure': bool(row[5]),
            'httponly': bool(row[6])
        })
    
    conn.close()
    return cookies

def get_session_storage(url):
    """Extract session storage using Selenium"""
    options = webdriver.ChromeOptions()
    options.binary_location = '/usr/bin/brave-browser'
    options.add_argument('--headless')
    
    driver = webdriver.Chrome(service=Service(), options=options)
    driver.get(url)
    
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, 'body')))
        
        try:
            session_storage = driver.execute_script(
                "return Object.fromEntries(Object.entries(sessionStorage));")
        except:
            session_storage = {}
    finally:
        driver.quit()
    
    return session_storage

def main():
    parser = argparse.ArgumentParser(description='Extract Brave browser data')
    parser.add_argument('url', help='Website URL to extract data from')
    args = parser.parse_args()
    
    result = {
        'url': args.url,
        'cookies': get_brave_cookies(args.url),
        'session_storage': get_session_storage(args.url)
    }
    
    print(json.dumps(result, indent=2))

if __name__ == '__main__':
    main()
