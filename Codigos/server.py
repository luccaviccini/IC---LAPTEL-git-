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
    while True:
        #t0 = time.time()
        #listt0 = []
        #listt0.append(t0)
        data, addr = s.recvfrom(2048)
        i = i + 1
        r1 = time.time()
        print(i,r1)


        print(data)
        #if data != None:
            #t1 = time.time()
            #i = i + 1




    c.close()

    #timediff = t1-t0

    #print('How long it took to receive 1 frame: ', timediff)


if __name__ == '__main__':
    Main()
