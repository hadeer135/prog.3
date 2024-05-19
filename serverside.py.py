### chat room connection (server and multiple clients (client to client chat ))

import threading
from socket import*
host ='127.0.0.1'
port =65000
server=socket(AF_INET,SOCK_STREAM)
server.bind((host,port))
server.listen()
clients=[]
names=[]


def session (message):
    for client in clients:
        client.send(message)

def client_deal (client):
    while True:
        try:
            message=client.recv(1024)
            session(message)
        except:
            index=clients.index(client)
            clients.remove(client)
            client.close()
            name=names(index)
            session(f'{name} has left the chat room '.encode ('utf-8'))
            names.remove(name)
            break

def receive():
    while True:
        print(" the server is available ")
        client , address=server.accept()
        print(f'connection is started with {str(address)}')
        client.send('name?'.encode('utf-8'))
        name=client.recv(1024)
        names.append(name)
        clients.append(client)
        print(f'the name of the client is {name}'.encode('utf-8'))
        session(f'{name} is connected to the chat room '.encode ('utf-8'))
        client.send('you are now connected '.encode('uth-8'))
        thread=threading.Thread(target=client_deal , args=(client,))
        thread.start()

if __name__=='__main__':
    receive()



