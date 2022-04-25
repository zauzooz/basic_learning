from ctypes.wintypes import INT
import socket
import random

INIT = 0

try:
    socketClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as error:
    print("Error: %s" % (error))

host = socket.gethostname()
port = 9999
end_point = (host, port)

socketClient.connect(end_point)

server_data = INIT

while (True):
    # send data
    client_data = str(server_data + random.randint(0, 10))
    socketClient.send(client_data.encode())
    # recieve data
    server_data = int(socketClient.recv(1024).decode())
    print("Server: %d" % (server_data))


socketClient.close()
