# TrainWithUmashankar

A beginner-friendly Flask website for technical learning, fitness content, and continuous self-improvement.

## Run locally (Windows PowerShell)

```powershell
py --version
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
flask --app app run --debug
```

Open http://127.0.0.1:5000. Stop the development server with `Ctrl+C`.

If PowerShell blocks activation, use `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` for the current terminal only. Ubuntu/WSL users can use `python3 -m venv .venv`, `source .venv/bin/activate`, and `python -m pip install -r requirements.txt`.

## Update content

- Edit personal text and social URLs in [config.py](config.py).
- Edit technical resource descriptions in [data/resources.json](data/resources.json).
- Update the shared Google Drive study-material link in `config.py` under `SITE_CONTENT["study_materials"]["drive_folder_url"]`.
- Templates are in `templates/`; visual styling is in `static/css/style.css`; mobile navigation is in `static/js/main.js`.

The initial version intentionally has no database, login, forms, or secret values. Study materials are shared through a public Google Drive folder; set its sharing permission to "Anyone with the link" if visitors should be able to open it.

## Test

With the virtual environment active:

```powershell
pytest
```

## GitHub

Create an empty repository named `trainwithumashankar` on GitHub, then run:

```powershell
git init
git add .
git commit -m "Create TrainWithUmashankar Flask website"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/trainwithumashankar.git
git push -u origin main
```

Never put passwords, API keys, or `.env` files in the repository. GitHub stores source code; it does not execute Flask.

## Production deployment

GitHub Pages cannot run Python or Flask. Use a Python-compatible host that can deploy from GitHub (for example, a provider that supports a Gunicorn start command). Connect the repository, install from `requirements.txt`, and use `gunicorn app:app` as the start command. The included `Procfile` supplies that command to hosts that support it. Do not use Flask's development server in production.

Before deploying, set `SECRET_KEY` through the host's environment settings and update the placeholder content. Check the provider's current pricing, sleep limits, build logs, and Python version support; free tiers and terms can change. A custom domain can be connected later through the host's domain settings.
