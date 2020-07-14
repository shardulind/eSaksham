class DevelopmentConfig(object):
    DEBUG = True
    TESTING = False
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'alohmora'
    MYSQL_DB = 'db'

class ProductionConfig(object):
    DEBUG = False
    MYSQL_HOST = 'esaksham'
    MYSQL_USER = 'esaksham'
    MYSQL_PASSWORD = 'database@123'
    MYSQL_DB = 'esaksham$db'
    ####pythonanywhere mysql db address format
####mysql+mysqldb://<username>:<mysql_password>@<hostname>/<username>$task_list
