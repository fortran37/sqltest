import os, sys, time
import sqlite3 as sql
from testEnv import *

'''
    SQLite3 process notes:
    create connection to file/create file = ( con = sqlite3.connect("example.db"))
    create cursor = (cur = con.cursor())

    execute
    create
        cur.execute("CREATE TABLE tablename(key1, key2, key3)")
        
        #tbc#
'''

#This is a dumb fix, but it is functional.
dbSuf = ".db"

#Asking for name of database to create or open if exists.
dbToOpen = input("Enter the name of the database to open or create: ")

#Create connection based on above input + suffix.
con1 = sql.connect(dbToOpen+dbSuf)

#Now create the cursor.
cur = con1.cursor()



