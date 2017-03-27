import mysql.connector
import struct
from io import BytesIO

itemList = [
    [1, 0, 3, 0, 10],
    [1, 0, 4, 0, 20]
]


conn = mysql.connector.connect(user = 'root', password = 'jgy', database = 'rewardcode')
cursor = conn.cursor()

cursor.execute('select name from rewardcodemobi')
values = cursor.fetchall()

print('result =', values[0][0].decode('UTF-8'))

'''
cursor.execute('call AddGift(%s, %s, %s, %s)', ['J123456789111', '3', 1587756977, item_data.getvalue()])
conn.commit()
'''
cursor.close()
conn.close()
