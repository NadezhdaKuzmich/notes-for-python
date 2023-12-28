# example 2 (UDP unix socket)
import os
import socket

unix_sock_name = 'unix.sock'
# create UNIX UDP-socket
sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

if os.path.exists(unix_sock_name):
    os.remove(unix_sock_name)

# bind socket-file with `bind`
# for unix socket method - file's name.
sock.bind(unix_sock_name)

# infinite loop for constantly reading data, without stopping the server
while True:
    try:
        result = sock.recv(1024)
    except KeyboardInterrupt:
        sock.close()
        break
    else:
        print('Message', result.decode('utf-8'))
