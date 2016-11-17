'''

This is a simple program which demonstrates socket client programming in python.
@author Nitinkumar Gove
@version 1.0

'''
import socket
import sys
from thread import *

# define a thread function to handle the connection
def clientthread(conn):
    conn.send("<server> hey, there ! how can I help ?")
 
    while True:
        data = conn.recv(2048)
        resp = "ok - " + data
        conn.sendall(resp) 
    
    conn.close();

# ----------------------------------------------------

host = ''
port = 6000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "< server socket created >"

try:
    s.bind((host, port))
except socket.error, msg:
    print "ERROR - failed to bind socket"
    sys.exit()

print "< socket bind - true >"

s.listen(10)

# accept connetions and attach a thread handling function to it
while 1:
    try:
        conn, addr = s.accept()
        print "connected to - " + str(addr[0])
        start_new_thread(clientthread, (conn,))
    except socket.error, msg:
        print "ERROR - ", msg[1]

s.close()


