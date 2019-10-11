#Jackson Zou
#SoftDev
#skeleton :: SQLITE3 BASICS
#Oct 2019

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="info.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================

# < < < INSERT YOUR POPULATE-THE-DB CODE HERE > > >

command = "CREATE TABLE stu_avg (name STRING, id INTEGER PRIMARY KEY, average REAL);"
c.execute(command)    # run SQL statement
command = "SELECT name, students.id, mark FROM students, courses WHERE students.id = courses.id"
c.execute(command)
info = c.fetchall()
print(info)

#==========================================================

db.commit() #save changes
db.close()  #close database
