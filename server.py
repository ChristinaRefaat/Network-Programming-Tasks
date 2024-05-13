import socket
import threading

host = '127.0.0.1'
port = 6000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nick_names = []


# Broadcast Messages To All Clients expect sender
def broadcast(message, sender_client):
    for client in clients:
        if client != sender_client:
            client.send(message)


# To Handle Messages From Clients
def Handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message, client)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nick_names[index]
            broadcast('{} left!'.format(nickname).encode('ascii'), client)
            nick_names.remove(nickname)
            break

def Receive():
    while True:
        client, address = server.accept()
        print("Connected with {}".format(str(address)))
        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nick_names.append(nickname)
        clients.append(client)
        print("Nickname is {}".format(nickname))
        broadcast("{} joined!".format(nickname).encode('ascii'), client)
        client.send('Connected to server!'.encode('ascii'))
        thread = threading.Thread(target=Handle, args=(client,))
        thread.start()

Receive()
