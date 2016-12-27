#sqlite test

import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()
'''
# create table
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')

# insert data
cursor.execute('insert into user (id, name) values (\'1\', \'Albert\')')
cursor.execute('insert into user (id, name) values (\'2\', \'Bella\')')

print('count =', cursor.rowcount)

cursor.close()
conn.commit()
coon.close()
'''

#query

cursor.execute('select * from user where id >= ?', ('1',))
values = cursor.fetchall()
print('result =', values)

cursor.close()
conn.close()
