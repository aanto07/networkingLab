import socket
import sys

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 8080

s.connect(('127.0.0.1',port))
str=("Hai from client")
byte = str.encode()
s.send(byte)
print (s.recv(1024))
print("Message sent from Client")
s.close()