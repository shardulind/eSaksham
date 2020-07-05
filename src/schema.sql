### MySQL database ###
# Database name: db 
# usernam

create database db;


#new volunteer table
create table new_volunteer_application(fname varchar(25), lname varchar(30), email_id varchar(50) PRIMARY KEY, password varchar(35), centre varchar(35), dob date, mob_no varchar(11));

