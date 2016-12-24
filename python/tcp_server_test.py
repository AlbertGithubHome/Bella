# tcp server test

import socket, threading, time

def tcplink(sock, addr):
    print('Accept new connection from %s : %s...' % (sock, addr))
    sock.send(b'Welcome to Beijing!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('I receive msg : %s!' % data.decode('utf-8')).encode('utf-8'))
        print('I receive msg : %s!' % data.decode('utf-8'))
    sock.close()
    print('Connection from %s : %s closed' % (sock, addr))

def start_server():
    # create and bind
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 9876))

    # set connection num
    s.listen(3)
    print('waiting for connection...')


    while True:
        sock, addr = s.accept()
        print('new connection come in')
        t = threading.Thread(target = tcplink, args = (sock, addr))
        t.start()

if __name__ == '__main__':
    start_server()