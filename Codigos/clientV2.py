import socket
import time

def Parametros():

        x = input('Digite uma das taxas de envio 10, 12, 15, 30 ou 60: ')
        x = float(x)
        time_delay = 1/(1.1*x)
        # Para o socket
        client_ip = 'localhost'
        client_port = 5001
        server_port = 5000
        server_ip = 'localhost'
        server = (server_ip, server_port)
        #Se quiser colocar um limite no numero de frames enviados
        maxenvio = 600
        return time_delay, client_ip, client_port, server_port, maxenvio, server_ip, server


def Cria_Socket():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return s

def Main():
    time_delay, client_ip, client_port, server_port, maxenvio, server_ip, server = Parametros()

    s = Cria_Socket()
    s.bind((client_ip, client_port))

    dataframe = b'\xaa\x01\x00\x34\x1e\x36\x44\x85\x36\x00\x00\x00\x41\xb1\x00\x00\x39\x2b\x00\x00\xe3\x6a\xce\x7c\xe3\x6a\x31\x83\x04\x44\x00\x00\x09\xc4\x00\x00\x42\xc8\x00\x00\x44\x7a\x00\x00\x46\x1c\x40\x00\x3c\x12\xd4\x3f'
    i = 0
    t = 0
    j = 0



    while True:
        s.sendto(dataframe, server)
        time.sleep(time_delay)
        if t == 0:
            ti = time.time()
            t = 1


        i = i + 1
        j = j + 1
        if i == 60:
            i = 0;
            #print(time.time())
            print('ENVIEI 60:   ', j)

        #comentar esse envio se for loop infinito
        if j == maxenvio:
            tf = time.time()
            break

    s.close()
    timediff = tf - ti
    print('Tempo que o processo levou: ', timediff)


if __name__ == '__main__':
    Main()
