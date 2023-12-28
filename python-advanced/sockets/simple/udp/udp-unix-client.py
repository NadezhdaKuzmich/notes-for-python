# udp client
import socket

# create UNIX UDP-socket
sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
# send data на UNIX-socket - file `unix.sock`
sock.sendto(b'Test Message', 'unix.sock')
