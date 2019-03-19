

str_content = 'BZh91AY&SYA\\xaf\\x82\\r\\x00\\x00\\x01\\x01\\x80\\x02\\xc0\\x02\\x00 \\x00!\\x9ah3M\\x07<]\\xc9\\x14\\xe1BA\x06\\xbe\\x084'
bytes_content = bytes(str_content, "latin1")
print(bytes_content.decode('unicode_escape').encode('latin1'))

import codecs
print(codecs.escape_decode(bytes_content)[0])

import re
pattern=re.compile(r'((?P<w>\d)(?P=w)*)')
print(pattern.findall('1234444432'))
print(re.findall(r'((\d)(\d)(\d))', '1234444432'))

print(re.findall(r'((?P<word>\d)(?P=word)*)', '111221233334'))

print(1 if True else 2)

if 1:
    print(0)

content = "1234567890"
for i in range(5):  
    print(content[i::5])  

#print('\n'.join([''.join([('008ct'[(x-y) % 5] if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else ' ') for x in range(-30, 30)]) for y in range(30, -30, -1)]))

print(''.join(list(map(chr, [48, 48, 56, 99, 116]))), type(''.join(list(map(chr, [48, 48])))))
print('\n'.join([''.join([(''.join(list(map(chr, [48, 48, 56, 99, 116])))[(x-y) % 5] if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else ' ') for x in range(-30, 30)]) for y in range(30, -30, -1)]))


for x in range(1,10, 1):
    print(x)


print("00123456"[:4])

print("00123456"[:-1])

print(b'1' + b'2')
print(''.join(['1','2']))
#print(''.join([b'1',b'2']))

print(hex(ord('x')))

print('qwert'[1:2])

print('qwett'[-3])

L = [1,2,3,4]
L.pop()
print(L)

print((1,2) + (2,1))

for x in [1]:
    print(1)

L = [1]
print(L.pop())
#print(str(L.pop()))

print([1,2,3,4,5,6,7,8,9][1::2])

print("abcdefg"[:1])
print("abcdefg"[2:])
print("abcdefg"[:1] + "abcdefg"[2:])

print(bytes(chr(97), encoding='utf-8') + bytes(chr(50), encoding='utf-8') + bytes(chr(65), encoding='utf-8'))

print('0'*5)
print(type(('0'*5)[::1]))

import re

print(list(map(int, re.findall(r'.{1}', ('0'*5)))))


alist = eval("['我', '的', '地', '盘盘']")
print(alist)

import os
android_home = os.environ.get("Path")
print(android_home)