from  socket import*
s =socket()
print('Socket succesfully created')
port = 56004
s.bind(('', port))
print(f'socket binded to port{port}')
s.listen(5)
print('Socket is listening')
while True:
    c, addr = s.accept()
    print('Got connection from', addr)
    message = ('Thank you for connecting')
    c.send(message.encode())
    c.close()