#! /usr/bin/python

import os, sys, socket
"""
Author: Dreyton Scott; Class:ITC510
Due: 11/16/16;

This Program runs a server on localhost with a port specified on
program execution, for example(./client <server-port>). Server 
is then listening for a request. The server is waiting for a 
file path. Once recieved the server checks if file exists on 
the hosting machine. If the file does not exist, then it sends
error message to the client that the file doesnt exist. If the
file does exist we send the file, line by line, to the client.
Server then closes connection.
"""

if(len(sys.argv)!=2):
    print ("usage: %s <server-port>" % sys.argv[0])
    sys.exit(1)

PORT = sys.argv[1]
ADDR = ('localhost',int(PORT))

try:
    _socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as msg:
    print >> sys.stderr, msg
try:
    _socket_.bind(ADDR)
    _socket_.listen(5)
except socket.error as msg:
    print >> sys.stderr, msg
    _socket_.close()
    
print >> sys.stdout, "Server Listening on Port",PORT

while 1:
    _connection_, _address_ = _socket_.accept()
    while 1:
        data = _connection_.recv(512)
        data = data.replace('\x00','')
        reply = "Seen: "+ data
        if not data:
            break
        else:
            print >> sys.stdout, data
            try:
                f = os.stat(data)
            except:
                print >> sys.stderr, "No file"
                reply = "Error: No such file"
                _connection_.send(reply)
            if (os.path.isfile(data)):
                if(os.access(data,os.R_OK)):
                    with open(data,'r') as infile:
                        for line in infile:
                            _connection_.send(line)
                    infile.close()
                else:
                    _connection_.send("Error: File does not have read permission")
    _connection_.send("Closing Connection")
    _connection_.close()

_socket_.close()
sys.exit(0)
