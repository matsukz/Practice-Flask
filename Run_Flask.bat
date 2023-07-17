@echo off

set FLASK_APP=flask_app.py
echo FLASK_APP

set FLASK_ENV=development
echo FLASK_ENV

flask run

pause