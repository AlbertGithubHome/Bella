# mysql test

import mysql.connector

conn = mysql.connector.connect(user = 'root', password = '123456', database = 'test')
cursor = conn.cursor()

cursor.execute('select * from book')
values = cursor.fetchall()

print('result =', values)


conn = mysql.connector.connect(user = 'root', password = '123456', database = 'test')
cursor = conn.cursor()

cursor.execute('select rolename from gameinfo limit 2')
values = cursor.fetchall()

print('result =', values)


for n in values:
    print(n)
    print(n[0].decode('utf-8'))