# Hirist Automated Job Apply

A small Python script to automate job applications on Hirist (personal use).

**Features**
- Automates filling and submitting job applications on Hirist
- Simple single-file script: `hirist_auto_apply.py`

**Requirements**
- Python 3.8+ (Windows, macOS, Linux)
- Typical libraries used for automation (install if required): `requests`, `selenium`, `beautifulsoup4` (if the script needs them)

**Installation**
1. Clone the repository or download the single script.
2. (Optional) Create and activate a virtual environment:

```bash
python -m venv .venv
# Windows
.\.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate
```

3. Install dependencies (if the script requires them):

```bash
pip install -r requirements.txt
# or, if no requirements file exists, install commonly used packages:
pip install requests selenium beautifulsoup4
```

**Usage**
Run the script from the project root:

```bash
python hirist_auto_apply.py
```

If the script requires configuration (credentials, resume path, search filters), update the configuration block or provide environment variables as described in the script.

**Run Chrome with remote debugging**
The script connects to a Chrome instance on `127.0.0.1:9222`. Start Chrome with the remote debugging port before running the script.

Windows (PowerShell):

```powershell
"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:/ChromeDebugProfile"
```

macOS:

```bash
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir="/tmp/chrome-debug"
```

Linux:

```bash
google-chrome --remote-debugging-port=9222 --user-data-dir="/tmp/chrome-debug"
```

Use a dedicated `--user-data-dir` to avoid interfering with your regular Chrome profile.

**Configuration**
Open `hirist_auto_apply.py` and look for the top-level configuration variables (email, password, resume path, job filters). Edit them safely — do not commit secret credentials to Git.

**Notes & Safety**
- Use responsibly and only for accounts you own. Automating actions on a website may violate its Terms of Service—review Hirist's policies before using this tool.
- Avoid storing plaintext credentials in the repository. Prefer environment variables or a local config file excluded via `.gitignore`.

**Disclaimer**
- For learning and research purposes only. This repository is provided as-is to demonstrate automation techniques and should not be used to bypass or violate any website's terms, access controls, or applicable laws.
- The project author (developer) is not responsible for how others use this code. You are solely responsible for compliance with any site's Terms of Service and with local laws and regulations.
- Do not store or commit sensitive credentials in this repository. Use environment variables or local configuration files excluded via `.gitignore`.

**Contributing**
PRs and issues welcome. Keep changes small and focused. Add a `requirements.txt` if you introduce new dependencies.

**License**
MIT — see LICENSE (or add one) for details.
