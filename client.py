import socket
import tqdm
import os
import sys
import argparse

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 512

argument = argparse.ArgumentParser()
argument.add_argument("--fname", type = str)
argument.add_argument("--host_addr", type = str)
argument.add_argument("--host_port", type = int)

host = argument.parse_args().host_addr
port = argument.parse_args().host_port
name = argument.parse_args().fname

size = os.path.getsize(name)

s = socket.socket()

print("Connecting to ip:", end = '')
print(host, end = ' ')
print("port:", end = '')
print(port)

s.connect((host, port))
print("Connection successful!")

s.send(f"{name}{SEPARATOR}{size}".encode())

sent = 0
file = open(name, 'rb')
content = file.read(BUFFER_SIZE)
while content:
    s.send(content)
    data = file.read(BUFFER_SIZE)
    sent = min(size, sent + BUFFER_SIZE)
    print('progress: ', end = '')
    print(sent, end = '/')
    print(size, end = ' ')
    print('bytes are already sent')

file.close()
s.close()