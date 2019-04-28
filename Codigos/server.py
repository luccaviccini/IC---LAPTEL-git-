import socket
import time

def Main():
    host = '192.168.0.105'
    port = 5000
    server = (host,5000)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))
    t = 0
    i = 0
    j = 0
    data = None
    print('Server Started. ')
    #lista = []

    while True:

        data, addr = s.recvfrom(4096)

        if t == 0:
            ti = time.time()
            t = 1

        i = i + 1
        j = j + 1
        if i == 60:
            i = 0;
            print(time.time())
            print('RECEBI 60:   ', j)
        if j == 3000:
            tf = time.time()
            break

    s.close()
    timediff = tf - ti
    print('Tempo que o processo levou: ', timediff)




if __name__ == '__main__':
    Main()
