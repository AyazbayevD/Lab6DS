import socket
import tqdm
import os
import threading


def save_file(client_socket):
    rcvd = client_socket.recv(BUFFER_SIZE).decode()
    name, size = rcvd.split(SEPARATOR)
    name = os.path.basename(name)
    size = int(size)

    progress = tqdm.tqdm(range(size), f"Receiving {name}", unit = "B", unit_scale = True, unit_divisor = 1024)
    with open(name, "wb") as f:
        for _ in progress:
            bytes_read = client_socket.recv(BUFFER_SIZE)
            if not bytes_read:
                break
            f.write(bytes_read)
            progress.update(len(bytes_read))

    client_socket.close()
    s.close()

host = ""
port = 5000
BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"

s = socket.socket()

s.bind((host, port))

s.listen(5)
print("Listening at ip:", end = '')
print(host, end = ' ')
print("port:", end = '')
print(port)


while True:
    client_socket, addr = s.accept()
    print("User with ip:", end = '')
    print(addr, end = ' ')
    print("has connected")
    thread = threading.Thread(target = save_file, args = (client_socket,))
    thread.start()