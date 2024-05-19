from socket import *
import threading

def receive_messages(client):
    while True:
        x = client.recv(2024)
        print("client : ", x.decode('utf-8'))
        y = input("server: ")
        client.send(y.encode('utf-8'))

try:
    s = socket(AF_INET, SOCK_STREAM)
    host = '127.0.0.1'
    port = 65435
    s.bind((host, port))
    s.listen(5)
    
    client, address = s.accept()
    
    print("connection from : ", address[0])

    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.start()

except error as e:
    print(e)

except KeyboardInterrupt :
    print("chat is terminated")

