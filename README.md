##### Development
***
##💻 Tech Stack 💻
#Python3 - Flask - Mysql

***

Ensure that you have these

## Technology Stack 
   -Python 3.6.9
   -Flask 1.1.2
   -Werkzeug 1.0.1 (comes along with flask)
   -mysql

## requirements.txt (pip python packages)
   -MySQLdb



# eSaksham.md

![](https://pandao.github.io/editor.md/images/logos/editormd-logo-180x180.png)

**Table of Contents**

[TOCM]

[TOC]


#Swagger API Specification
`<link>` :https://app.swaggerhub.com/apis/shardulind5/login/1.0.0



# Project Layout

```
~/e-Saksham
├── src/
│   ├── __init__.py
│   ├── db.py
│   ├── schema.sql
│   ├── auth.py
│   ├── foo.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── auth/
│   │   │   ├── login.html
│   │   │   └── register.html
│   │   └── foo/
│   │       ├── foo.html
│   │       ├── foo.html
│   │       └── foo.html
│   ├── static/
│   │  └── style.css
│   │
│    └── js/
│          └── foo.js
│
├── tests/
│   ├── conftest.py
│   ├── data.sql
│   ├── test_factory.py
│   ├── test_db.py
│   ├── test_auth.py
│   └── test_foo.py
└── setup.py *
```


### Description about Project Layout
```
📁 src  : All Code will rest here
📁 src/__init__.py : Factory Code: All Flask related Initiation and Configuration 
📁 📝src/db.py : Creating Connection with Database - MySQL and db related configuration
📁 📝src/schema.sql: SQL queries to setup the database tables 
📁📝 src/auth.py: Authentication module (blueprint) contains __Endpoints__ related to Login Functionality and assisting function,
📁templates/ : will have all HTML files
📁static/ : static data, css and js files will rest here

📁tests/: Wo badmein dekh lenge
```

