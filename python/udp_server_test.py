# udp server test

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# bind port
s.bind(('127.0.0.1', 9876))
print('Bind UDP on 9876...')

while True:
    data, addr = s.recvfrom(1024)
    print('Received from %s:%s.' % addr)
    s.sendto(b'Hello, %s' % data, addr)
