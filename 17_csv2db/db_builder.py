#Jackson Zou
#SoftDev pd9
#K17 -- No Trouble
#10-10-2019

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O

def addstudents():
    DB_FILE="students.db"

    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops

    #==========================================================

    # < < < INSERT YOUR POPULATE-THE-DB CODE HERE > > >
    c.execute("CREATE TABLE students (name TEXT, age INTEGER, id INTEGER PRIMARY KEY);")
    with open('students.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            c.execute("INSERT INTO students VALUES ({}, {}, {});".format("\"" + row["name"] + "\"", row["age"], row["id"]))

    #print out the values from the table
    c.execute("SELECT * FROM students;")
    rows = c.fetchall()
    print(rows)
#==========================================================

    db.commit() #save changes
    db.close()  #close database

def addclasses():
    DB_FILE="courses.db"

    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops

    #==========================================================

    # < < < INSERT YOUR POPULATE-THE-DB CODE HERE > > >
    c.execute("CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER);")
    with open('courses.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            c.execute("INSERT INTO courses VALUES ({}, {}, {});".format("\"" + row["code"] + "\"", row["mark"], row["id"]))

    #print out the values from the table
    c.execute("SELECT * FROM courses;")
    rows = c.fetchall()
    print(rows)
#==========================================================

    db.commit() #save changes
    db.close()  #close database

if __name__ == "__main__":
    addstudents()
    addclasses()
