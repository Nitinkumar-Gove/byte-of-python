'''

This is a simple program which demonstrates socket programming in python.
@author Nitinkumar Gove
@version 1.1

'''

import socket
import sys

# creates a TCP socket with IPv4 address family
try:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # (address family - IPv4, type - connection oriented TCP)
except socket.error,msg:
    print " failed to create socket - ",msg[1]
    sys.exit()

print "socket created"  #stage 1 end

# fetch IP address for a host 
host = "www.google.com"
port = 80
try:
    fbip = socket.gethostbyname(host)
except socket.gaierror,msg:
    print "failed to find host ip - ", msg[1]
    sys.exit()

print "fb ip address  - ",fbip #stage 2 end

# connect to host on port
try:
    s.connect((host,port))
except socket.error, msg:
    print "failed to connect - ",msg[1]
    sys.exit()

print "socket connected" #stage 3 end

# send data to server
payload = "GET / HTTP/1.1\r\n\r\n"
try:
    s.sendall(payload)
except socket.error, msg:
    print "failed to send data - ",msg[1]
    sys.exit()

print "payload sent successfully" #stage 4 end

# receive data from server
try:
    data = s.recv(4096)
except socket.error, msg:
    print "failed to receive data - ",msg[1]
    sys.exit()

print "data -",data #stage 5 end

# close the socket 
s.close()
print "socket disconnected"
    