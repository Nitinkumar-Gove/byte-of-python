'''

This is a simple program which demonstrates socket server programming in python.
@author Nitinkumar Gove
@version 1.1

'''

import socket
import sys

host = ''
port = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "socket created"

try:
    s.bind((host,port))
except socket.error, msg:
    print msg[1]
    sys.exit()

print "socket bind complete"

s.listen(10)
print "listening now ..."

# handle all the connection in an endless loop / wait for the connection and server
while 1:
    con,add = s.accept()
    print "connected to ", str(add[0])
    data = con.recv(1024);
    print "server received >> ",data
    con.sendall("heard ya ! ")


con.close()
s.close()