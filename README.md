# File Transfer using Socket Programming (TCP and UDP)

The idea is to provide a basic understanding of socket programming in python and analyzing the throughput achieved by differnet types of implementations. I have implemented variants of file transfer in terms of concurrency and algorithms. These variants are listed as follows:

1. Based on type of connection:
    - TCP
    - UDP
2. Based on Algorithms:
    - Nagle's Algorithm
    - Delayed ACK
3. Based on Concurrency:
    - concurrent server using Fork
    - concurrent server using threads
4. Based on Consistency:
    - Persistent TCP connection
    - Non-persistent TCP connection

## Novels

| Serial number | Novel Name       | File named as at server side | Size (MB) |
|---------------|------------------|------------------------------|-----------|
| 1.            | Sherlock Holmes  | sherlock.txt                 | 3.9       |
| 2.            | War and Peace    | warpeace.txt                 | 3.4       |
| 3.            | Jane Eyre        | janeeyre.txt                 | 3.2       |
| 4.            | Middlemarch      | middlemarch.txt              | 1.8       |
| 5.            | Romeo and Juliet | romeo.txt                    | 1.5       |

## TCP usage

1. Analyzing the algorithms
    - move into the folder [tcp_algorithms]
    - run server using `python3 server.py` and enter the port number
    - run client in another terminal using `python3 client.py`
    - enter the port number of the server
    - follow the instructions to enable or disable the algorithms
    - user can ask for only one file at a time

2. Concurrency - fork
    - move into the folder [tcp_fork]
    - run the server using `python3 fork_server.py`
    - run client in another terminal using `python3 fork_client.py`
    - ask the files in spave separated fashion like `sherlock.txt warpeace.txt`
    - the client side will connect with the server individually for each file (running the all the clients simultaneously)

3. Concurrency - threads
    - move into the folder [tcp_thread]
    - run the server using `python3 thread_server.py`
    - run client in another terminal using `python3 thread_client.py`
    - ask the files in spave separated fashion like `sherlock.txt warpeace.txt`
    - the client side will connect with the server individually for each file (running the all the clients simultaneously)

4. Non persistent TCP
    - move into the folder [tcp_non_persistent]
    - run the server using `python3 nonp_server.py`
    - run client in another terminal using `python3 nonp_client.py`
    - ask the files in spave separated fashion like `sherlock.txt warpeace.txt`
    - one by one file transfer (each creating a new tcp connection)

## UDP usage

In UDP, persistent and non-persistent remains same because there is no particular handshake in UDP which initiates the connection.