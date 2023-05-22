import socket
s=socket.socket()
print('socket successfully created')
port=56789
s.bind(('',port))
print(f'socket binded to port {port}')
s.listen(5) #means it has max 5 conncections. sixth can't be accepted
print('socket is listening')
while True:
    c,addr=s.accept()
    print('Got conection from',addr)
    message=('thank you for connecting')
    c.send(message.encode())
    c.close()

'''to get connection in the output~ in a new terminal type $ telnet localhost 56789'''
