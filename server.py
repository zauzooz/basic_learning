import socket
from _thread import *
from time import sleep


I = 0
hostList = []
listNum = []


def average(listNum):
    AVR = 0
    for item in listNum:
        AVR = AVR + item
    AVR = int(AVR/len(listNum))
    return AVR


def thread_client(conn, addr, host):
    global listNum
    print("Host %d connect to the server." % (host))
    while(True):
        # recieve data
        client_data = conn.recv(1024).decode()
        listNum.append(int(client_data))
        print("Client %d: %s" % (host, client_data))
        sleep(5)
        # update data
        server_data = str(average(listNum))
        # send data
        conn.send(server_data.encode())
        print("At host %d work, listNum has %d data." % (host, len(listNum)))
        if (host + 1 == len(listNum)):
            listNum.clear()


try:
    socketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as error:
    print("Error: %s" % (error))

host = socket.gethostname()
port = 9999

end_point = (host, port)

socketServer.bind(end_point)
listen = socketServer.listen(5)

while (True):
    connect, address = socketServer.accept()
    hostList.append(I)
    I = I + 1
    start_new_thread(thread_client, (connect, address, hostList[I-1]))


socketServer.close()
