#bin/sh
virtualenv -p /usr/bin/python3 py
source py/bin/activate
pip install -r requirements.txt
python main.py