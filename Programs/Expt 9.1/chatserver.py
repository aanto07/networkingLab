import socket
import select 
import sys 
from _thread import *

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port=8001

s.bind(('',port))

s.listen(5) 
list_of_clients = []
def clientThread(conn,addr):
    wel="welcome"
    welcome = wel.encode()
    conn.send(welcome)
    while True:
        message=conn.recv(1024)
        if message:
            print("[ " + str(addr[0]) + ":"+ str(addr[1]) +"  ] :" )
            print(message)
            message = message.decode()
            message_to_send =  "<" + addr[0] +" : "+ str(addr[1]) + "> :" + message
            msg2 = message_to_send.encode()
            broadcast(msg2,conn)
        else:
            remove(conn)

def broadcast(message,conn):
    for client in list_of_clients:
        if client!=conn:
            client.send(message)

def remove(conn):
    if conn in list_of_clients:
        list_of_clients.remove(conn)

while True:
    conn,addr=s.accept()
    print ('Got Connection from',addr)
    list_of_clients.append(conn)
    start_new_thread(clientThread,(conn,addr))
    
    
conn.close()
