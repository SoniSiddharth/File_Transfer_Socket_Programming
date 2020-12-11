# importing libraries
import socket
import os
import timeit
import time

# creating client socket
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# taking server IP and port as input
target_ip = input('Enter Target IP = ')
target_port = input('Enter port = ')

# connecting with server
client_socket.connect((target_ip,int(target_port)))

# dictionary defined for a suitable name format of the downloaded file
Name_dictionary = {"sherlock.txt": "Sherlock_Holmes", "warpeace.txt": "War_and_Peace", "romeo.txt": "Romeo_and_Juliet", "middlemarch.txt": "Middlemarch", "janeeyre": "Jane_Eyre"}

# Buffer size
BUFFERSIZE = 32786

# input the name of the requested file
file_name = input('Enter file name on server = ')

# disable Nagle's algorithm by using this code and asking the user
Nagle_disable = int(input('Enter 1 to disable Nagle\'s algorithm else 0 = ' ))
if (Nagle_disable):
    client_socket.setsockopt(socket.IPPROTO_TCP,socket.TCP_NODELAY,True)

# asking for delayed ACK disabling from user
Delayed_ACK = int(input('Enter 1 to disable Dealyed ACK otherwise 0 = '))
if (Delayed_ACK):
    client_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_QUICKACK, True)
client_socket.send(file_name.encode())

#start the timer
start = timeit.default_timer()

# a confirmation that file exists
confirmation = client_socket.recv(100)

if confirmation.decode() == "file-doesn't-exist":
    print("File doesn't exist on server.")
else:           
    write_name = Name_dictionary[file_name] + "_TCP_" + str(os.getpid()) + ".txt"
    if os.path.exists(write_name): os.remove(write_name)

    # open the file to read bytes
    with open(write_name,'wb') as file:
        while (1):
            if (Delayed_ACK):
                client_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_QUICKACK, True)
            data = client_socket.recv(BUFFERSIZE)
            if not data:
                break
            file.write(data)
    
    # stop the timer
    stop = timeit.default_timer()
    time_taken = stop - start
    print(write_name,'successfully downloaded.')
    print("Time taken to download file : ", time_taken*1000)

#closing the connection
client_socket.shutdown(socket.SHUT_RDWR)
client_socket.close()