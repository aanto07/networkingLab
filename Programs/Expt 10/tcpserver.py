import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Created Socket ")
port= 8080

s.bind(('',port))
print("Binding Socket to ",port)

s.listen(5) 

while True:
    c,addr=s.accept()
    message=c.recv(1024)
    print(message)
    print ('Got Connection from',addr)
    print('Thanks for connecting')
    c.close()
    exit(0)
