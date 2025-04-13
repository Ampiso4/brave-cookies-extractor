# Brave Data Extractor

Extracts cookies and session storage from Brave browser for a given website.

## Installation

1. Install required system packages (if not already installed):

```bash
sudo apt update && sudo apt install python3-venv
```

2. Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Install ChromeDriver matching your Brave browser version:

```bash
python -m pip install webdriver-manager
```

## Usage

```bash
python extractor.py "https://example.com"
```

## Output

The script outputs JSON containing:

- Website URL
- All cookies for the domain
- Session storage contents

Example output:

```json
{
  "url": "https://example.com",
  "cookies": [
    {
      "name": "session_id",
      "value": "abc123",
      "domain": ".example.com",
      "path": "/",
      "expires": 1735689600,
      "secure": true,
      "httponly": true
    }
  ],
  "session_storage": {
    "user_prefs": "dark_mode"
  }
}
```

## Notes

1. Brave browser must be installed
2. The script will:
   - Access Brave's cookies database directly
   - Open the URL in a headless browser to capture session storage
3. For security, the script only accesses cookies for the specified domain
4. Session storage is only available for sites that use it
