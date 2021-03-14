# coding:utf-8

import socket, sys

HOST = "127.0.0.1"
PORT = 4444

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((HOST, PORT))
except Exception as e:
    print(e)
    sys.exit()
while True:
    c = input('> ')
    s.sendall(c.encode())
    data = s.recv(1024)
    data = data.decode()
    print('Received: ', data)
    if c.lower() == 'quit':
        break
s.close()