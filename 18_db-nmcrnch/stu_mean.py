#Jackson Zou
#SoftDev pd9
#K18 -- Average
#2019-10-15

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="info.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================

# < < < INSERT YOUR POPULATE-THE-DB CODE HERE > > >

#command = "CREATE TABLE stu_avg (name STRING, id INTEGER PRIMARY KEY, average REAL);"
#c.execute(command)    # run SQL statement
command = "SELECT name, students.id, mark FROM students, courses WHERE students.id = courses.id"
c.execute(command)
info = c.fetchall() #Get all the names, ids, and marks from students and courses tables
print(info)
command = "CREATE TABLE stu_avg(name TEXT, id INTEGER PRIMARY KEY, average REAL);"
c.execute(command) #create new table

id = 0
sum = 0
count = 0
name = ""

for each in info: #loop through the list of values and get the sum of marks and number of classes each student has
    if id == each[1]:
        sum += each[2]
        count += 1
        name = each[0]
    else:
        if id != 0:
            command = "INSERT INTO stu_avg VALUES (\"{}\", {}, {});".format(name, id, sum / count) #add into table when id is different
            print("Student name: {}, ID: {}, Average: {}".format(name, id, sum / count))
            c.execute(command)
        id += 1
        sum = each[2]
        count = 1
        name = each[0]
command = "INSERT INTO stu_avg VALUES (\"{}\", {}, {})".format(info[len(info) - 1][0], id, sum / count) #account for last value
c.execute(command)
print("Student name: {}, ID: {}, Average: {}".format(info[len(info)-1][0], id, sum / count))
command = "SELECT * FROM stu_avg"
c.execute(command)
final = c.fetchall()
#==========================================================

db.commit() #save changes
db.close()  #close database
