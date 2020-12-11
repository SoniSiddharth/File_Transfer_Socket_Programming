import os, time, sys
from socket import *

# Buffer size
BUFFERSIZE = 1024

server_ip = '127.0.1.1'
port_addr = int(input('Enter the port number --> '))

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind((server_ip, port_addr))
server_socket.listen(10)
print("Server listening at ", server_ip, "and port ", port_addr)

current_childs = []
def child_process():
    while current_childs:
        pid,stat = os.waitpid(0, os.WNOHANG)
        if not pid:
            break
        current_childs.remove(pid)

def handleClient(connection):
    while(1):
        data = connection.recv(BUFFERSIZE).decode()
        data = "../Books/" + data
        if not os.path.exists(data):
            os._exit(0)
        else:
            if data != '':
                file = open(data,'rb')
                data = file.read(BUFFERSIZE)
                while (data and data[-3:]!=b"EOF"):
                    connection.send(data)
                    data = file.read(BUFFERSIZE)
                print("File sent succesfully")
                break
    connection.close()
    os._exit(0)

# main function
def main_function():
    while 1:
        # accepting more than 1 client
        connection, addr = server_socket.accept()
        print('connected to', addr)
        child_process()
        # creating parallel process using fork
        child_pid = os.fork()
        if child_pid == 0:
            handleClient(connection)
        else:
            current_childs.append(child_pid)

main_function()
