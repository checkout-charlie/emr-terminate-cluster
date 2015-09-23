#bin/bash

BASEPATH=''

rm -rf $BASEPATH"py"
virtualenv -p /usr/bin/python3 $BASEPATH"py"
. $BASEPATH"py/bin/activate"
pip install -r $BASEPATH"requirements.txt"
python3 $BASEPATH"main.py"