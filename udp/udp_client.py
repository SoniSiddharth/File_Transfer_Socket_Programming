# importing libraries
import socket
import os
import timeit

# get the IP and port of the server
target_port = int(input('Enter port = '))
input_ip = '127.0.1.1'
target_ip = (input_ip, target_port)

# Name definition
Name_dictionary = {"sherlock.txt": "Sherlock_Holmes", "warpeace.txt": "War_and_Peace", "romeo.txt": "Romeo_and_Juliet", "middlemarch.txt": "Middlemarch", "janeeyre.txt": "Jane_Eyre"}

# BUffer 
BUFFERSIZE = 1024

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# get the file name as mentioned in answer 2 from the user example - "sherlock.txt"
file_name = input('Enter file name on server = ')

files = list(file_name.split())
num_of_files = len(files)
total_time = timeit.default_timer()
for j in range(num_of_files):
    current_file = files[j]
    # encode the string before sending
    bytesToSend = str.encode(current_file)
    UDPClientSocket.sendto(bytesToSend, target_ip)

    confirmation, addr = UDPClientSocket.recvfrom(100)
    response = str(confirmation)
    # print(response)
    if response == "file-doesn't-exist":
        print("File does not exist on server")
        os.exit()
    else:
        write_name = Name_dictionary[current_file] + "_UDP_" + str(os.getpid()) + ".txt"
        if os.path.exists(write_name): os.remove(write_name)
        print("starting....")
        try:
            # starting the timer
            start = timeit.default_timer()
            with open(write_name,'wb') as file:
                while (1):
                    # setting the timeout of 0.1 seconds for each data received
                    UDPClientSocket.settimeout(5)
                    data, addr = UDPClientSocket.recvfrom(BUFFERSIZE)
                    file.write(data)
            print("done!")
        except:
            stop = timeit.default_timer()
            time_taken = stop - start - 5
            file_size = os.stat(write_name).st_size
            print(write_name,'successfully downloaded.')
            print("Time taken to download file of size ",file_size, "is ", time_taken*1000, "ms")
            print("Throughput is ", file_size/time_taken, "bytes/sec")
            continue
        # close the connection
total_time = timeit.default_timer() - total_time
print("Total time taken ",total_time - 25) # subtracting the timeout time for client
UDPClientSocket.close()
