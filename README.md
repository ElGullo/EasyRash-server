Introduction
-------------

EasyRash is an online platform for organizing academic conferences.
It covers all the roles and phases involved in the process, including
Event and Paper submissions and Peer-Review.
The reviewers can use the site to annotate the papers
and give feedback to the chair for the final decision.

This is the EasyRash server repo.

Requirements
------
```
Flask
Flask-HTTPAuth
Flask-Mail
Flask-RESTful
Flask-WTF
flask-mongoengine
passlib
```

You can use pip and virtualenv for and easier installation.

```
virtualenv .env
. .env/bin/activate
pip install -r requirements
deactivate
```


Usage
------

- Install requirements
- Fill in the config in secrets.py
- Host and port can be changed in run.py (defaults to localhost:10000)
- python run.py
