# -*- coding: utf-8 -*-


import sqlite3

conn = sqlite3.connect('db.sqlite3')

print("Opened database successfully")

cursor = conn.execute("SELECT * from ex_employee")

for row in cursor:
    print(row)

conn.close()
