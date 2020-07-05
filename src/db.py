# we will complete this later
# 
# https://flask.palletsprojects.com/en/1.1.x/tutorial/database/  use this for reference

from flask import current_app, g
from flask_mysqldb import MySQL
import MySQLdb


def get_db():
    db = MySQLdb.connect(
        host = current_app.config["MYSQL_HOST"], 
	    user = current_app.config["MYSQL_USER"],
	    passwd = current_app.config["MYSQL_PASSWORD"], 
	    db = current_app.config["MYSQL_DB"], 
	    cursorclass = MySQLdb.cursors.DictCursor)
    
    return db
