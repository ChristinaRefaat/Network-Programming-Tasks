from socket import *

try:
    # Creating a socket (IPV4 , TCP)
    s = socket(AF_INET, SOCK_STREAM)
    print('Client socket is successfully created')

    host = '127.0.0.1'
    port = 6600
    s.connect((host, port))
    print(f'Connected to server at {host}:{port}')

    while True:
        x = input('Client send: ')
        s.send(x.encode() + b'\n')
        receive = b''
        while True:
            y = s.recv(2048)
            if not y:
                break
            receive += y
            if b'\n' in y:
                break

        print(f'Client received: {receive.decode()}')

    s.close()

except Exception as e:
    print(f'Socket error: {e}')
