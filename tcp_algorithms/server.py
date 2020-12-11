# import libraries
import socket
import os
import time

#creating TCP socket
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip = socket.gethostbyname(socket.gethostname())

# taking port as input from the user
port = int(input('Enter desired port = '))

# binds the socket to the port
server_socket.bind((ip,port))

# disable Nagle's algorithm at server side by asking user
Nagle_disable = int(input('Enter 1 to disable Nagle\'s algorithm else 0 = ' ))
if (Nagle_disable):
    server_socket.setsockopt(socket.IPPROTO_TCP,socket.TCP_NODELAY,True)

# Delayed ACK disable by asking user
Delayed_ACK = int(input('Enter 1 to disable Dealyed ACK otherwise 0 = '))

# listening for requests at the defined port
server_socket.listen(100)
BUFFERSIZE = 32786
print('Running on IP: '+ ip)
print('Running on port: '+ str(port))

while(1):
    # to accept different connection requests
    connection, addr = server_socket.accept()
    print("New Connection established")
    print(connection)

    # disable delayed ACK before each sending
    if (Delayed_ACK):
        server_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_QUICKACK, True)
    data = connection.recv(100).decode()
    data = "../Books/" + data
    if not os.path.exists(data):
        connection.send("file-doesn't-exist".encode())
        print("File does not exist")
    else:
        connection.send("file-exists".encode())
        print('Sending',data)
        if data != '':
            file = open(data,'rb')
            data = file.read(BUFFERSIZE)
            while (data):
                if (Delayed_ACK):
                    server_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_QUICKACK, True)
                connection.send(data)
                # adding a sleep time of 100 microseconds for Question 4
                time.sleep(0.0001)
                data = file.read(BUFFERSIZE)
            print("File sent succesfully")
    
    # close the connection with current client
    connection.shutdown(socket.SHUT_RDWR)
    connection.close()
    print("")
server_socket.close()