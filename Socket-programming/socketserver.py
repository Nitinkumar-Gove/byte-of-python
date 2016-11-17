'''

This is a simple program which demonstrates socket server programming in python.
@author Nitinkumar Gove
@version 1.1

'''
import socket
import sys

# create server socket for (host, port)
host = ''
port = 8888

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    s.bind((host,port))
except socket.error, msg:
    print "bind failed - ", msg[1]
    sys.exit()

print "socket created" #stage 1 end

# listen for connections
s.listen(10)
print "listening..." #stage 2 end

# accept the connection
conn, addr = s.accept()
print "connected to - ",str(addr[0]), str(addr[1]) #stage 3 end

conn.sendall("hello")
conn.close()
s.close()

