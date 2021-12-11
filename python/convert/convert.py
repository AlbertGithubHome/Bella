
import struct

print(type(1))
print(type("s"))
print(type(b"dd"))
print(type(1.07))

num = 10
val = str(10)
print(val, type(val))

num = 10
val = '{0}'.format(num)
print(type(val), val)

num = 10
val = hex(num)
print(type(val), val)

num = 10
val = bin(num).replace('0b','')
print(type(val), val)


val = int('10')
print(type(val), val)

val = int('0xa', 16)
print(type(val), val)
val = int('a', 16)
print(type(val), val)

val = int('0b1010', 2)
print(type(val), val)
val = int('1010', 2)
print(type(val), val)

val = int('10', 5)
print(type(val), val)

#val = int('128', 2)

print(type(b'2'))

num = 10
val = bytes(num)
print(type(val), val)

b = b'\x12\x34'
n = int.from_bytes(b,byteorder='big',signed=False)

num = 4665
val = num.to_bytes(length=4, byteorder='little',signed=False)
print(type(val), val)

num_array = [57, 18, 0, 0]
val = bytes(num_array)
print(type(val), val)


#import struct

num = 4665
val = struct.pack("<I", num)
print(type(val), val)


bys = b'9\x12\x00\x00'
val = int.from_bytes(bys, byteorder='little', signed=False)
print(type(val), val)

bys = b'9\x12\x00\x00'
val = struct.unpack("<I", bys)
print(type(val), val)

n = [12,34]
b = bytes(n)
print(b)


s = '大漠孤烟直qaq'
val = s.encode('utf-8')
print(type(val), val)

bys = b'\xe5\xa4\xa7\xe6\xbc\xa0\xe5\xad\xa4\xe7\x83\x9f\xe7\x9b\xb4qaq'
val = bys.decode('utf-8')
print(type(val), val)


bys = b'\xe5\xa4\xa7\xe6\xbc\xa0\xe5\xad\xa4\xe7\x83\x9f\xe7\x9b\xb4qaq'
s = str(bys)
print(type(s), s)

def str2bytes(str_content):
    result_list = [];
    pos = 0
    str_content = str_content.replace("\\n", "\n").replace("\\t", "\t").replace("\\r", "\r")
    content_len = len(str_content)
    while pos < content_len:
        if str_content[pos] == '\\' and pos + 3 < content_len and str_content[pos + 1] == 'x':
            sub_str = str_content[pos + 2: pos + 4]
            result_list.append(int(sub_str, 16))
            pos = pos + 4
        else:
            result_list.append(ord(str_content[pos]))
            pos = pos + 1
    return bytes(result_list)

val = str2bytes(s[2:-1])
print(type(val), val)


bys = b'9\x12\x00\x00'

a =[x for x in b'9\x12\x00\x00']
print(a)


print('美好'.encode('utf-8'))
print(bytes('美好', 'utf-8'))
print(b'\xe7\xbe\x8e\xe5\xa5\xbd'.decode('utf-8'))

import binascii
print(binascii.b2a_hex(b'\xe7\xbe\x8eqaq'), len(b'\xe7\xbe\x8eqaq'))

print(binascii.a2b_hex(b'e7be8e716171'), len(b'e7be8e716171'))

print(b'\xe7\xbe\x8eqaq'.hex(), type(b'\xe7\xbe\x8eqaq'.hex()))

print(bytes.fromhex('e7be8e716171'))