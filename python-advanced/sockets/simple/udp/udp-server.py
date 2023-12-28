# example 1 (UDP server socket)
import socket

# create UDP-socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', 8888))
# read 1024 byte
result = sock.recv(1024)
print('Message', result.decode('utf-8'))
# close socket
sock.close()
