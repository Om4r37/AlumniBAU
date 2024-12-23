git clone https://github.com/Om4r37/AlumniBAU.git
cd AlumniBAU\
New-Item -Path "config.py" -ItemType "file" -Force
Set-Content -Path "config.py" -Value "# change before deployment
DATABASE = 'database.db'
SCHEMA = 'schema.sql'
DEBUG = False
SECRET_KEY = 'development_key'
USERNAME = 'admin'
PASSWORD = 'default'
PORT = 1337"
python -m venv .venv
.venv\Scripts\activate
pip install -r setup\requirements.txt
start http://localhost:1337/
python run.py