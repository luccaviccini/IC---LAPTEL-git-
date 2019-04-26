import socket
import time

def Main():
    host = '10.15.1.70'
    client_port = 5001
    server_port = 5000
    server = (host,server_port)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, client_port))

    dataframe = b"aa0100341e3644853600000041b10000392b0000e36ace7ce36a31830444000009c4000042c80000447a0000461c40003c12d43f"
    i = 0;
    while i < 60:
        t0 = time.time()
        s.sendto(dataframe, server)

        #tf = time.time()
        i = i + 1
    tf = time.time()
    timediffClient = tf - t0

    print(timediffClient)







if __name__ == '__main__':
    Main()
