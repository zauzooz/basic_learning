import socket
import random

from sqlalchemy import true

INIT = 0

try:
    socketClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as error:
    print("Error: %s" % (error))

host = socket.gethostname()
port = 9999
end_point = (host, port)
while (true):
    try:
        socketClient.connect(end_point)
        break
    except:
        pass

server_data = INIT

while (True):
    # send data
    client_data = server_data + random.randint(0, 20)
    print("Send %d" % client_data)
    socketClient.send(str(client_data).encode())
    # recieve data
    server_data = int(socketClient.recv(1024).decode())
    print("Server: %d" % (server_data))


socketClient.close()
