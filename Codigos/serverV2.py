import socket
import time
import crc_calculation as C

def Parametros(): ## Parametros a serem definidos antes do inicio do codigo

    server_ip = '10.15.1.132'
    server_port = 5000
    server = (server_ip,5000)
    maxrecebe = 600
    return server_ip, server_port, server, maxrecebe

def Main():

    server_ip, server_port, server, maxrecebe = Parametros()

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
        #inicio da contagem do tempo
        if t == 0:
            ti = time.time()
            t = 1

        #calulando crc
        crcdec = C._crc16(data[0:-2], 0xFFFF, C.CRC16_XMODEM_TABLE)
        crc_calc = hex(crcdec)[2:]
        

        #extraindo crc da mensagem
        crc1 = hex(data[50])[2:]
        crc2 = hex(data[51])[2:]
        crc_orig = crc1 + crc2


        if crc_calc != crc_orig:
            print('HALELLUJAH')
            print(j)

        i = i + 1
        j = j + 1
        if i == 60:
            i = 0;
            #print(time.time())
            print('RECEBI 60:   ', j)
        if j == maxrecebe:
            tf = time.time()
            break

    s.close()
    timediff = tf - ti
    print('Tempo que o processo levou: ', timediff)




if __name__ == '__main__':
    Main()
