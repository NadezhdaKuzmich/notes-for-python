# example 1 (UDP server socket)
import socket

# IP UDP-socket server
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('127.0.0.1', 8888))

# infinite loop for constantly reading data, without stopping the server
while True:
    try:
        result = sock.recv(1024)
    except KeyboardInterrupt:
        sock.close()
        break
    else:
        print('Message', result.decode('utf-8'))
