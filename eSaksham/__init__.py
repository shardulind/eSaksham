import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate

####pythonanywhere mysql db address format
####mysql+mysqldb://<username>:<mysql_password>@<hostname>/<username>$task_list

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev'
        SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb:////esaksham:database@123@esaksham.mysql.pythonanywhere-services.com//esaksham$db'
        SQLALCHEMY_POOL_RECYCLE = 280,
        SQLALCHEMY_TRACK_MODIFICATIONS = False
    )
    
    db.init_app(app)
    migrate.init_app(app, db)

    return app

