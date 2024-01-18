################# Create a database in mysql workbench #################    

# create database sam;
# use sam;

# create table student(name varchar(20), school varchar(20));

# insert into student values ("Samuel", "Waitua"), ("Jane", "Mugecha")

# select * from student; 

import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="Samuel", password="Vidsamco@2019", database="sam")  

mycursor = mydb.cursor()

mycursor.execute("select * from student")

result = mycursor.fetchall()

for i in result:
    print(i) 
    
    

    
    
    
    
    
