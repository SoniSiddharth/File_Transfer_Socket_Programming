import socket
from threading import Thread
import time
import os
import sys

ip_addr = '127.0.1.1'
port_addr = int(input('Enter the port number --> '))

BUFFERSIZE = 1024

# client thread class for using it further for creating new threads for each client
class client_Handle(Thread):

    def __init__(self, ip_addr, port_addr, socket_connection):
        Thread.__init__(self)
        self.ip_addr = ip_addr
        self.port_addr = port_addr
        self.socket_connection = socket_connection
        print("New thread created for "+ ip_addr +":"+ str(port_addr))

    def run(self):
        while(1):
            # sleep for handling blocks
            time.sleep(5)
            data = self.socket_connection.recv(BUFFERSIZE).decode()
            data = "../Books/" + data
            print(data)
            if not os.path.exists(data):
                os._exit(0)
            else:
                if data != '':
                    file = open(data,'rb')
                    data = file.read(BUFFERSIZE)
                    while (data and data[-3:]!=b"EOF"):
                        self.socket_connection.send(data)
                        data = file.read(BUFFERSIZE)
                    self.socket_connection.send(data)
                    print("File sent succesfully")
                    break
        self.socket_connection.close()
        os._exit(0)

# initializing server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((ip_addr, port_addr))

#list of current running threads
current_threads = []

# main program for threading
while True:
    server_socket.listen(5)
    print("server listening at ", ip_addr, port_addr)

    # accepting new connections
    (conn, (ip_address, port_no)) = server_socket.accept()
    print('Got connection from ', (ip_address, port_no))
    new_thread = client_Handle(ip_address, port_no, conn)
    new_thread.start()
    current_threads.append(new_thread)

# to join the threads
for j in current_threads:
    j.join()
