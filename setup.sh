#!/usr/bin/env bash
# Shell helper for Unix-like environments (Linux/macOS)

# create virtual environment if missing
if [ ! -d .venv ]; then
    python -m venv .venv
    echo "Virtual environment created in .venv"
else
    echo ".venv already exists"
fi

# activate environment
source .venv/bin/activate

# install requirements
pip install -r requirements.txt

# copy .env template
if [ ! -f .env ]; then
    cp .env.example .env
    echo "Copied .env.example to .env; please update with your API key."
else
    echo ".env already present; ensure it contains your GOOGLE_API_KEY."
fi

echo "Setup complete. Use 'adk run smart_resume_analyzer' or 'adk web' to start."