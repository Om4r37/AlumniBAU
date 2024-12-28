git clone https://github.com/Om4r37/AlumniBAU.git
cd AlumniBAU/
touch config.py
echo "# change before deployment
DATABASE = 'database.db'
DEBUG = False
SECRET_KEY = 'development_key'
USERNAME = 'admin'
PASSWORD = 'default'
PORT = 1337
MAIL_USERNAME = ''
MAIL_PASSWORD = ''" > config.py
python3 -m venv .venv
source .venv/bin/activate
pip install -r setup/requirements.txt
xdg-open http://localhost:1337/
python3 run.py