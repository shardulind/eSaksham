import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

conn = None
try:
    conn = mysql.connector.connect(host = 'localhost',
                                         database = 'esaksham',
                                         user = 'root',
                                         password = 'password5665')
    if conn.is_connected():
            print('Connected to MySQL database')

    mysql_create_table = """CREATE table new_volunteer_applications(fname varchar(25) NOT NULL,lname varchar(30), email_id varchar(50) NOT NULL,passwd varchar(35) NOT NULL, centre varchar(25), dob date, mob_no varchar(20) NOT NULL, PRIMARY KEY(email_id))"""
    mysql_insert_query = """INSERT INTO new_volunteer_applications (fname, lname, email_id, passwd, centre, dob, mob_no)
                             VALUES 
                             ('Sam', 'Charlie', 'samC@gmail.com', 'Sam@123', 'Alandi', '1999-12-12', '9988776655')"""
    
    cursor = conn.cursor()
    cursor.execute(mysql_create_table)
    print("\nTable Inserted successfully\n")
    cursor.execute(mysql_insert_query)  
    conn.commit()
    print(cursor.rowcount, "Record inserted successfully into new_volunteer_applications table")
    cursor.close()

except mysql.connector.Error as error:
    print("Failed to insert record into new_volunteer_applications table {}".format(error))

finally:
    if conn is not None and conn.is_connected():
            conn.close()    
