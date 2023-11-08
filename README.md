# flask-task
demo project for simple REST-API by python

## req python 3.10! and higher 

## Step 0. Init virtuel env
    python3 -m venv .venv


## Step 1. To activate venv windows/linux
    .\.venv\Scripts\activate
    source .venv/bin/activate

use PowerShell by admin and  execute: Set-ExecutionPolicy RemoteSigned (comfirm for ALL)

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

## Запуск проекта

# by python
    python main.py
    py .\main.py

# by flask (venv)
    export FLASK_APP=main.py FLASK_ENV=development FLASK_DEBUG=1
    flask run --port=2001

# by process manager (not venv)
    sudo pm2 start ".venv/bin/python3 main.py" --name FLASK
