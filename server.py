import socket
from _thread import *
from time import sleep

SPEED = 0.005
I = 0
hostList = []
listNum = []
#_lastNum = 0
_return = 0


def average():
    global SPEED
    global listNum
    global _lastNum
    global _return
    while (True):
        sleep(SPEED)
        try:
            N = len(listNum)
            Sum = 0
            for item in listNum:
                Sum = Sum + item
            _return = int(Sum / N)
            print(str(listNum) + " -> "+str(_return))
            listNum.clear()
        except:
            pass


def thread_client(conn, addr, host):
    global listNum
    global _return
    global SPEED
    while(True):
        # recieve data
        client_data = conn.recv(1024).decode()
        listNum.append(int(client_data))
        sleep(SPEED)
        # update data
        server_data = _return
        # send data
        conn.send(str(server_data).encode())


try:
    socketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as error:
    print("Error: %s" % (error))

host = socket.gethostname()
port = 9999

end_point = (host, port)

socketServer.bind(end_point)
listen = socketServer.listen(5)
try:
    start_new_thread(average, ())
    while (True):
        connect, address = socketServer.accept()
        hostList.append(I)
        I = I + 1
        start_new_thread(thread_client, (connect, address, hostList[I-1]))
except KeyboardInterrupt:
    socketServer.close()
