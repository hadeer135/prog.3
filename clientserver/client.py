from  socket import*
s = socket()
port = 56004
s.connect(('127.0.0.1', port))
print(s.recv(1024))
s.close()