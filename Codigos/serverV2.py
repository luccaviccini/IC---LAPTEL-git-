import socket
import time
import crc_calculation as C

def Parametros(): ## Parametros a serem definidos antes do inicio do codigo

    server_ip = '10.15.1.132'
    server_port = 5000
    server = (server_ip,5000)
    return server_ip, server_port, server

def Main():

    server_ip, server_port, server = Parametros()

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((server_ip, server_port))

    #contadores
    t = 0
    i = 0
    j = 0
    data = None
    print('Server Started. ')
    #lista = []

    while True:

        data, addr = s.recvfrom(4096)
        crc = C._crc16(data[0:-2], 0xFFFF, C.CRC16_XMODEM_TABLE)
        print(hex(crc))

        if t == 0:
            ti = time.time()
            t = 1

        i = i + 1
        j = j + 1
        if i == 60:
            i = 0;
            #print(time.time())
            print('RECEBI 60:   ', j)
        if j == 1200:
            tf = time.time()
            break

    s.close()
    timediff = tf - ti
    print('Tempo que o processo levou: ', timediff)




if __name__ == '__main__':
    Main()
