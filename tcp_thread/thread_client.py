# importing libraries
import socket
import os
import timeit
import time
import multiprocessing

# taking server IP and port as input
target_ip = "127.0.1.1"
target_port = input('Enter port = ')

# dictionary defined for a suitable name format of the downloaded file
Name_dictionary = {"sherlock.txt": "Sherlock_Holmes", "warpeace.txt": "War_and_Peace", "romeo.txt": "Romeo_and_Juliet", "middlemarch.txt": "Middlemarch", "janeeyre.txt": "Jane_Eyre"}

# Buffer size
BUFFERSIZE = 1024

while(1):
    # input the name of the requested file
    file_name = input('Enter file name on server = ')

    files = list(file_name.split())
    num_of_files = len(files)
    exist = 0
    for j in files:
        if j not in Name_dictionary:
            exist = 1
            print(j, "does not exist at server. Try again")
            break
    if (exist==0):
        break

def clientHandle(current_file, target_ip,target_port):
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client_socket.connect((target_ip,int(target_port)))
    client_socket.send(current_file.encode())

    #start the timer
    start = timeit.default_timer()
    print("downloading file ......")         
    write_name = Name_dictionary[current_file] + "_TCP_" + str(os.getpid()) + ".txt"
    if os.path.exists(write_name): os.remove(write_name)
    # open the file to read bytes
    flag = 0
    with open(write_name,'wb') as file:
        try:
            while (1):
                client_socket.settimeout(10)
                data = client_socket.recv(BUFFERSIZE)
                # print(data)
                if (not data):
                    flag = 1
                    break
                file.write(data)
            if (flag):
                stop = timeit.default_timer()
                time_taken = stop - start - 10
                file_size = os.stat(write_name).st_size
                print(write_name,'successfully downloaded.')
                print("Time taken to download file of size ",file_size, "is ", time_taken*1000, "ms")
                print("Throughput is ", file_size/time_taken, "bytes/sec")
                client_socket.close()
        except:
            stop = timeit.default_timer()
            time_taken = stop - start - 10
            file_size = os.stat(write_name).st_size
            print(write_name,'successfully downloaded.')
            print("Time taken to download file of size ",file_size, "is ", time_taken*1000, "ms")
            print("Throughput is ", file_size/time_taken, "bytes/sec")
            client_socket.close()

# code for simultaneously running the clients
# using multiprocessing library
for j in range(num_of_files):
    current_file = files[j]
    p = multiprocessing.Process(target=clientHandle, args=(current_file, target_ip, target_port,))
    p.start()