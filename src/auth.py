import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify, current_app
)
from werkzeug.security import check_password_hash, generate_password_hash

from .db import get_db
#instead we are doing....sod khnh

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


#pasara: temporary endpoints for development purpose
@auth_bp.route('/get_all_applications', methods=['GET'])
def get_all_new_volunteer_applications():
 
    mysql = get_db()
    
    cur = mysql.cursor()
    cur.execute('select * from new_volunteer_application;')
    print(cur.fetchall())
    return jsonify({'applications':cur.fetchall()})



#assisting functions
def does_user_already_exist(email_id):
    #somehtin somehting
    return True





##actual endpoints.. pending
@auth_bp.route('/register', methods=['POST','GET'])
def registration():
    if request.method == 'POST':    
        data = request.get_json()
        
        ##check if user already registered
        if does_user_already_exist(data['email_id']):
            return jsonify(
                {'logical status code':'403',
                'message':'Email id Already registered', 
                'data':
                    {
                    'email_id':data['email_id'],
                    'fname':data['fname']
                    }})
        

    return "work in progress"
        ##add user into new_volunteer_application
        ##PENDING

"""
        ##on successful addition of the data in table
            return jsonify(
                {
                    'logical status code':'200',
                    'message':'User added into database successfully',
                    'data':
                    {
                        'email_id':data['email_id'],
                        'fname':data['fname']
                    }
                }
            )
        ## if not added successfully
            return jsonify(
                {
                    'logical status code':'',
                    'message':'Something Went Wrong',    
                    'data':
                    {
                        'email_id':data['email_id'],
                        'fname':data['fname']
                    }
                }
            )
    else:
        pass
        #render registration page
"""



@auth_bp.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        return data
        ###possible scenario
        ###1) username is not registered
        ###2) pasword does not match
    
    else:
        return "work in progress"
        #render login.html from templates

