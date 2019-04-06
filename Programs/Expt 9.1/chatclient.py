import socket
import select 
import sys 
from _thread import *

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 8001
s.connect(('127.0.0.1',port))
def sendMessage(so):
    while True:
        message=input()
        msg = message.encode()
        so.send(msg)

start_new_thread(sendMessage,(s,))
while True:  
    data = s.recv(1024)
    
    print (data)


s.close()