# BytesIO test

from io import BytesIO
byte_stream = BytesIO() 
byte_stream2 = BytesIO() 
byte_stream3 = BytesIO() 
byte_stream3 = BytesIO() 

byte_stream.write('中文'.encode('utf8'))
print('byte_stream =', byte_stream.getvalue())


byte_stream2.write('中文'.encode('gbk'))
print('byte_stream2 =', byte_stream2.getvalue())


byte_stream3.write('中文'.encode('gb2312'))
print('byte_stream3 =', byte_stream3.getvalue())