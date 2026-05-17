# Robot UI

Python UI project for robot control/monitoring experiments.

## What This Repository Contains

- `main.py` - main Python entry point.
- `interface.ui` - Qt Designer UI file.
- `ui_interface.py` - generated or exported Python UI module.
- `QSS/` and `style.json` - styling assets.
- `QSS_Resources_rc.py` - Qt resource module.
- `requirements.txt` - Python dependencies.
- `.github/workflows/python-compile.yml` - lightweight Python compile check.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
```

## Notes

If the UI connects to robot hardware or a backend service, document the required ports, topics, IP addresses, or configuration files using safe placeholder values.