
from socket import *
import threading

def receive_messages(client):
    while True:
        x = client.recv(2048)
        print("server : ", x.decode("utf_8"))

try:
    client = socket(AF_INET, SOCK_STREAM)
    host = '127.0.0.1'
    port = 6500
    client.connect((host, port))

    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.start()

    while True:
        y = input("client : ")
        client.send(y.encode('utf_8'))

except error as e:
    print(e)

except KeyboardInterrupt:
    print("chat is terminated")