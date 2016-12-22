
import struct

print(struct.pack('<I', 10240099))

n = 10240099

b1 = (n & 0xff000000) >> 24
b2 = (n & 0xff0000) >> 16
b3 = (n & 0xff00) >> 8
b4 = n & 0xff
bs = bytes([b1, b2, b3, b4])

print(bs)
print(b1)
print(b2)
print(b3)
print(b4)


print(ord('@'))


# unpack
print(struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80'))

with open('test.bmp', 'rb') as file:
    content = file.read(30)

print(content)

ret = struct.unpack('<ccIIIIIIHH', content)
print(ret)
print('type =', ret[0] + ret[1])




