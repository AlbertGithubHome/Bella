import mysql.connector
import struct
from io import BytesIO

itemList = [
    [1, 0, 3, 0, 10],
    [1, 0, 4, 0, 20]
]


def pack_item(itemlist):
    data = BytesIO()
    for item in itemList:
        result = struct.pack('IIIII', item[0], item[1], item[2], item[3], item[4])
        data.write(result)
    return data

conn = mysql.connector.connect(user = 'root', password = 'jgy', database = 'rewardcode')



cursor = conn.cursor()

item_data = pack_item(itemList)
#cursor.execute('call AddGiftCode(%s, %s, %s, %s)', ['J123456789111', '3', 1587756977, item_data.getvalue()])
cursor.execute('update RewardCodeMobi set item = %s', [item_data.getvalue()])
conn.commit()
cursor.close()
conn.close()

