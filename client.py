import socket
import threading

nickname = input("Choose your nickname: ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 6000))

def Receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("An error occured!")
            client.close()
            break
        
def Send():
    while True:
        message = '{}: {}'.format(nickname, input(''))
        client.send(message.encode('ascii'))
        
# Starting Threads For Sending and Recieving
receive_thread = threading.Thread(target=Receive)
receive_thread.start()

write_thread = threading.Thread(target=Send)
write_thread.start()
