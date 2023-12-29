# example 1 (UDP client socket )
import socket

# create TCP client socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect to 8888 port
sock.connect(('', 8888))
# send sms
sock.send(b'Test message')
# close socket connection
sock.close()
