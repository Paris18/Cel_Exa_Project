# Cel_Exa_Project
Celery Example Project

Environment Setup:

Python3
virtualenv
redis

* create environment and install all requirements with command
pip3 install -r requirements.txt

* change to be done in settings file 
   - email username
   - email password
   - we can set these throght env variables
 
* start the worker with command from project directory
  - celery -A htmldowloader worker -l info
  
* start process with command 
  - python3 manage.py runserver
  
Api's

POST:http://127.0.0.1:8000/api/v1/htmldowloader/register/
DATA:
    {
    "urls": [
    "https://www.adnabu.com",
    "https://www.facebook.com"
    ],
    "email": "pariskamal8@gmail.com"
    }
    
RESPONSE:
  {
     "status": "mail has be sent u will receive shortly"
  }




