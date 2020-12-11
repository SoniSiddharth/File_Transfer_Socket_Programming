# importing libraries
import socket
import os
import time

# get the local IP of the server
localIP     = socket.gethostbyname(socket.gethostname())

# get the port number from the user for connection on that port
localPort   = int(input('Enter desired port = '))

# buffer size
BUFFERSIZE  = 1024

# tuple for IP and port number
tple = (localIP, localPort)
# print(tple)

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))
print("UDP server up and listening")

while(1):
    try:
        UDPServerSocket.settimeout(30)
        data, addr = UDPServerSocket.recvfrom(1024)
        file_data = str(data)[2:-1]
        # print(file_data)

        # Address of the server IP and port number
        print(addr)
        file_data = "../Books/" + file_data
        if not os.path.exists(file_data):
            print("File does not exist")
            os.exit()
            # encode the string to send the data to client
            bytesToSend = str.encode("file-doesn't-exist")
            UDPServerSocket.sendto(bytesToSend, addr)
        else:
            bytesToSend = str.encode("file-exists")
            UDPServerSocket.sendto(bytesToSend, addr)
            print('Sending',file_data)
            if file_data != '':
                file = open(file_data,'rb')
                file_data = file.read(BUFFERSIZE)
                while (file_data):
                    UDPServerSocket.sendto(file_data, addr)
                    # time.sleep(0.0001)
                    file_data = file.read(BUFFERSIZE)
                print("File sent succesfully")
            print()
    except:
        break
# closing the server
UDPServerSocket.close()

