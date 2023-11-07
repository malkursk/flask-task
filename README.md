# flask-task
demo project for simple REST-API by python


## Step 0. Init virtuel env
    python3 -m venv .venv

## Step 1. To activate venv windows/linux
    .\.venv\Scripts\activate
    source .venv/bin/activate

## Step 2. To save packages
    pip freeze >package.txt

## Step 3. To deactivate a virtual environment:
    deactivate

## Step 4. To init from req    
    virtualenv .venv
    Step 1 (windows/linux)
    pip install -r package.txt

## to install new packages
    pip install <package-name>

## Ручной запуск проекта из окружения
    export FLASK_APP=main.py
    export FLASK_ENV=development
    flask run --port=2001
