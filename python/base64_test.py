#base64 test

import base64

encode_str = base64.b64encode(b'abc')
print(encode_str)

src_str = b'binary\x00string'
print('len(src_str) =', len(src_str))

encode_str = base64.b64encode(b'binary\x00string')
print(encode_str)

encode_str = base64.b64encode(b'binary\x00strin')
print(encode_str)

encode_str = base64.b64encode(b'g')
print(encode_str)

n = ord('g')
n = n % 4 
print(n)

print()
print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))