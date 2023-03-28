import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root12345",
    database="SB0013"
)

print(mydb)

mycursor=mydb.cursor()

#mycursor.execute("CREATE DATABASE SB0013")
#mycursor.execute("SHOW DATABASES")
#mycursor.execute("USE SB0013")
#mycursor.execute("CREATE TABLE STUDENT_PROJECT(FIRST_NAME varchar (255),LAST_NAME varchar (255),EMAIL varchar (255) NOT NULL PRIMARY KEY,PASSWORD varchar (255));")
#mycursor.execute("INSERT INTO STUDENT_PROJECT VALUES ('Ankit','Rajak','ankit@simpilearn.com','12345')")

#mycursor.execute("SELECT * FROM SB0013.STUDENT_PROJECT")

for x in mycursor:
    print(x)

mydb.commit()
mycursor.close()