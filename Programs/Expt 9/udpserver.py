import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

port=8080

s.bind(('',port))


msgFromServer       = "Hello UDP Client "

bytesToSend         = str.encode(msgFromServer)

while True:
    msg,addr=s.recvfrom(1024)
    print ('Got Connection from',addr)
    print('Message from Client: ',msg)
    s.sendto(bytesToSend,addr)
    print("Thanks for connecting")
    