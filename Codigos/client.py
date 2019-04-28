import socket
import time

def Main():
    host = '192.168.0.105'
    client_port = 5001
    server_port = 5000
    server = (host,server_port)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, client_port))

    dataframe = b"aa0100341e3644853600000041b10000392b0000e36ace7ce36a31830444000009c4000042c80000447a0000461c40003c12d43f"
    i = 0
    t = 0
    j = 0

    while True:
        s.sendto(dataframe, server)
        time.sleep(0.016)
        if t == 0:
            ti = time.time()
            t = 1


        i = i + 1
        j = j + 1
        if i == 60:
            i = 0;
            #print(time.time())
            print('ENVIEI 60:   ', j)
        if j == 3000:
            tf = time.time()
            break

    s.close()
    timediff = tf - ti
    print('Tempo que o processo levou: ', timediff)


if __name__ == '__main__':
    Main()
