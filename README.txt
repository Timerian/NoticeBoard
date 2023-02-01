This is the final project for the Python Backend Development course from SkillFactory.

A list of all the libraries required for the server can be found in the 'requirements.txt' file.
For install them you can use command:
    pip install -r requirements.txt

Some setting constants in 'setting.py' importing from .env file which was created for safety reasons.

You need to create your own .env file in 'NoticeBoard' directory (which contain manage.py file) and add the next constants in it:
    SECRET_KEY (you will need to generate)
    EMAIL_HOST_USER
    EMAIL_HOST_PASSWORD
    DEFAULT_FROM_EMAIL
    SERVER_EMAIL

The basic logic of server is contained in 'board' app. All templates related to registration and authentication of user is contained in 'account' app.

In this project, the ability to send a weekly newsletter to users was implemented. For starting this process you need open new console window, open directory with manage.py file and enter to console the next command:
    py manage.py runapscheduler

Superuser: admin
Password: admin