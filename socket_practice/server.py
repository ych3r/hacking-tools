# coding=utf-8

import socket

language = {'Who are you?':'I\'m Jarvis, sir.', 'Attack!':'Yes, sir!', 'bye':'bye, sir!'}

HOST = "127.0.0.1"
PORT = 4444

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
print("Listening at port 4444...")

conn, addr = s.accept()
print("Connect by: ", addr)
while True:
    data = conn.recv(1024)
    data = data.decode()
    if not data:
        break
    print("Received message: ", data)
    conn.sendall(language.get(data, 'Nothing').encode())
conn.close()

s.close()