# example 1 (UDP client socket )
import socket

# create UDP socket (IP)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# send msg to `localhost:8888`
sock.sendto(b'Test message', ('localhost', 8888))
