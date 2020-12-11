# import libraries
import socket
import os
import time

#creating TCP socket
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip = '127.0.1.1'

# taking port as input from the user
port = int(input('Enter desired port = '))

# binds the socket to the port
server_socket.bind((ip,port))

# listening for requests at the defined port
server_socket.listen(100)
BUFFERSIZE = 1024
print('Running on IP: '+ ip)
print('Running on port: '+ str(port))

while(1):
    # to accept different connection requests
    connection, addr = server_socket.accept()
    
    data = connection.recv(BUFFERSIZE).decode()
    data = "../Books/" + data
    print('Sending file')
    if data != '':
        file = open(data,'rb')
        data = file.read(BUFFERSIZE)
        while (data and data[-3:]!=b"EOF"):
            connection.send(data)
            data = file.read(BUFFERSIZE)
        connection.send(data)
        print("File sent succesfully")
    # close the connection with current client
    connection.close()
server_socket.close()