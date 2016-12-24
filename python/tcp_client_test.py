# tcp client test

import socket

def start_client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 9876))

    print(s.recv(1024).decode('utf-8'))
    while True:
        info = input('please input your msg:')
        if info == 'q':
            s.send(b'exit')
            s.close()
        else:
            s.send(info.encode('utf-8'))
            print(s.recv(1024).decode('utf-8'))

if __name__ == '__main__':
    start_client()
