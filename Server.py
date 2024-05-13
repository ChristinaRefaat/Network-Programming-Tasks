from socket import *

try:
    s = socket(AF_INET, SOCK_STREAM)
    print('Server socket is successfully created')

    host = '127.0.0.1'
    port = 6600
    s.bind((host, port))
    print(f'Socket is bound to port {port}')

    s.listen(5)
    print('Socket is listening')

    c, addr = s.accept()
    print(f'Connected to {addr}')

    while True:
        receive = b''
        while True:
            y = c.recv(2048)
            if not y:
                print('Client closed the connection.')
                break
            receive += y
            if b'\n' in y:
                break
        print(f'Server received: {receive.decode()}')
        x = input('Server Response: ')
        c.send(x.encode() + b'\n')

    c.close()
except Exception as e:
    print(e)