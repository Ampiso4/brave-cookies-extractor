# 🌐 Brave Data Extractor

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.6%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A powerful tool to extract cookies and session storage data from Brave browser for specified websites.

[Features](#features) • [Prerequisites](#prerequisites) • [Installation](#installation) • [Usage](#usage) • [Examples](#examples)

</div>

## ✨ Features

- 🔒 Secure extraction of browser cookies
- 💾 Capture session storage data
- 🎯 Domain-specific data extraction
- 🚀 Easy-to-use command line interface
- 📄 JSON-formatted output

## 📋 Prerequisites

- Python 3.6 or higher
- Brave Browser
- Linux/Unix-based system

## 🛠️ Installation

1. Install required system packages:

```bash
sudo apt update && sudo apt install python3-venv
```

2. Clone the repository and navigate to the project directory:

```bash
git clone <repository-url>
cd brave-cookies-extractor
```

3. Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

4. Install Python dependencies:

```bash
pip install -r requirements.txt
```

5. Install ChromeDriver (matches your Brave browser version):

```bash
python -m pip install webdriver-manager
```

## 🚀 Usage

Run the extractor by providing a target URL:

```bash
python extractor.py "https://example.com"
```

## 📝 Examples

The script generates JSON output containing website data:

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

## ⚙️ Configuration

No additional configuration is required. The script automatically:

- Detects your Brave browser installation
- Manages browser sessions securely
- Handles cookie and storage access permissions

## ❗ Important Notes

1. **Security**:

   - The script only accesses cookies for the specified domain
   - Data is extracted in a controlled, headless browser environment

2. **Browser Requirements**:

   - Brave browser must be installed
   - Compatible with latest Brave versions

3. **Data Access**:
   - Cookies are accessed from Brave's database
   - Session storage is captured from live browser session
   - Only accessible for sites that implement session storage

## 🔧 Troubleshooting

Common issues and solutions:

1. **ChromeDriver Version Mismatch**

   - Update webdriver-manager: `pip install --upgrade webdriver-manager`
   - Manually install matching ChromeDriver version

2. **Permission Errors**
   - Ensure Brave is not running
   - Check file permissions in Brave user data directory

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📬 Contact

If you have any questions or feedback, please open an issue in the repository.

---

<div align="center">
Made with ❤️ for the Open Source Community
</div>
