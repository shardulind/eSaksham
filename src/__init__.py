import os
from flask import Flask,g
#from flask_mysqldb import MySQL

#import configuration module
from configmodule import DevelopmentConfig, ProductionConfig

#make if false if using Production server, on development local server keep it true
test_config = True


def create_app():
    app = Flask(__name__, instance_relative_config=True) # makes env aware about ../ directory as project dir
    app.config.from_mapping(
        SECRET_KEY = 'DEV',
        ##add database params too
    )

    #this is to load Production server configuration
    if test_config :
        app.config.from_object(DevelopmentConfig)


    import auth
    app.register_blueprint(auth.auth_bp)

    @app.route('/')
    def hello():
        return "<html><body><h3>E-Saksham: Work in Progress!<h3> <br>  try <a href=/auth/login>Login Page</a></body></html>"

    return app

