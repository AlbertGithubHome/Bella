#tcp test

import socket

# create and connect
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('www.sina.com.cn', 80))

# send request
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

buffers = []
while True:
    data = s.recv(1024)
    if data:
        buffers.append(data)
    else:
        break

all_data = b''.join(buffers)

hearder, html = all_data.split(b'\r\n\r\n', 1)
print(hearder.decode('utf-8'))

with open('sina.html', 'wb') as file:
    file.write(all_data)
