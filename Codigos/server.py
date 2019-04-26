import socket
import time

def Main():
    host = '10.15.1.70'
    port = 5000
    server = (host,5000)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    i = 0
    data = None
    print('Server Started. ')
    lista = []

    while True:

        data, addr = s.recvfrom(2048)
        y = len(lista)
        if y == 60:
            tempofinal = time.time()
            break

        else:
            lista.append(data)

        if y == 1:
            timestart = time.time()

    tempoforaloop = time.time()
    print(tempoforaloop)
    s.close()
    print('timediff: ', tempofinal - timestart)
    print(len(lista))
    print(lista)



if __name__ == '__main__':
    Main()
