#! /usr/bin/python

import os,sys,socket
"""
Author: Dreyton Scott; Class: ITC510;
Due: 11/16/16;

This program creates a client/socket and attempts to connect to server. Must provide same
server address and server port upon execution of program. Once successfully connected the
remote file path is sent. If the file exists at the remote location then the client recieves
the file line by line. Client then writes this file to a local file. Once finished writing,
program prints to standard output that the file has been retrieved. Program then closes file
and closes connection to server.
"""


if(len(sys.argv)!=5):
    print("./client <server-addr> <server-port> <remote-file-path> <local-file-path>")
    sys.exit(1)

PORT = sys.argv[2]
ADDR = sys.argv[1]
SADDR = (str(ADDR), int(PORT))
try:
    _socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as msg:
    print >> sys.stderr, msg
_socket_.connect(SADDR)
_socket_.send(sys.argv[3])


with open(sys.argv[4], 'w') as outfile:
    while True:
        data = _socket_.recv(512)

        if("Error" in data):
            print >> sys.stdout, data
        else:
            outfile.write(data)
            print >> sys.stdout, "Successfully retrieved data"
        if not data:
            break
        outfile.close()
_socket_.close()
print >> sys.stdout, "Connection Closed"
sys.exit(0)
