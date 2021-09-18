'''
import mysql.connector

mydb = mysql.connector.connect(host="localhost", port=4401, user="root", password="Divi@0410", database="dini")

print(mydb)

mycursor = mydb.cursor()

mycursor.execute("select *from employees")

database = mycursor.fetchall()

for x in database:
    print(x)
'''


import pand1 as pd
a = {'employee': {'karan': {'id': '032','salary': 25000, 'designation': 'ML'},
                  'naresh': {'id': '142','salary': 27000, 'designation': 'AI'}}}

















