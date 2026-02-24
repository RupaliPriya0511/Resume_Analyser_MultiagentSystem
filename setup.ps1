# PowerShell helper for environment setup
# run this from the repository root

# create virtual environment
if (-not (Test-Path -Path .venv)) {
    python -m venv .venv
    Write-Host "Virtual environment created in .venv"
} else {
    Write-Host ".venv already exists"
}

# activate environment
. .\.venv\Scripts\Activate.ps1

# install requirements
pip install -r requirements.txt

# copy example .env if necessary
if (-not (Test-Path -Path .env)) {
    Copy-Item .env.example .env
    Write-Host "Copied .env.example to .env; please update with your API key."
} else {
    Write-Host ".env file already present; ensure it contains your GOOGLE_API_KEY."
}

Write-Host "Setup complete. Use `adk run smart_resume_analyzer` or `adk web` to start."