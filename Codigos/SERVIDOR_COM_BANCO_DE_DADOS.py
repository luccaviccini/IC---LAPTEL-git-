import socket
import time
import matplotlib.animation as animation
import crc_calculation as C
import hex_msg as hxm
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import matplotlib.patches as mpatches
import sqlite3

def Parametros(): ## Parametros a serem definidos antes do inicio do codigo

    server_ip = 'localhost'
    server_port = 5000
    server = (server_ip,5000)
    maxrecebe = 108000
    return server_ip, server_port, server, maxrecebe

def Main():

    server_ip, server_port, server, maxrecebe = Parametros()

    #criando socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((server_ip, server_port))

    #contadores
    t = 0 # contador para inicar a contagem do tempo
    i = 0 # contador para contar 60 msg recebidas
    j = 0 # contador maxrecebe
    cntcrc = 0 # conta o numero de erros no crc
    cdata = 0 # contador para o commit do banco de dados

    data = None
    print('Server Started. ')

    #criando banco de dados se ja nao existir
    conn = sqlite3.connect('PhasorDataConcentrator.db')
    c = conn.cursor()

    def create_table(): # funcao para criar tabela dentro do banco de dados
        c.execute("CREATE TABLE IF NOT EXISTS teste(ModVa REAL, FaseVa REAL, ModVb REAL, FaseVb REAL, ModVc REAL,\
        FaseVc REAL)")

    def dynamic_data_entry(ModVa,ModVb,ModVc,FaseVa,FaseVb,FaseVc): # funcao para inserir valores na tabela do banco de dados
        c.execute("INSERT INTO teste(ModVa, FaseVa, ModVb, FaseVb, ModVc, FaseVc) VALUES (?, ?, ?, ?, ?, ?)", (ModVa, FaseVa, ModVb, FaseVb, ModVc, FaseVc))

    create_table()

    while True:
        #Funcao que recebe as mensagens
        data, addr = s.recvfrom(4096)

        #inicio da contagem do tempo
        if t == 0:
            ti = time.time()
            t = 1

        #calulando crc
        crcdec = C._crc16(data[0:-2], 0xFFFF, C.CRC16_XMODEM_TABLE)
        crc_calc = hex(crcdec)[2:]

        #extraindo crc da mensagem
        crc1 = hex(data[len(data) - 2])[2:]
        crc2 = hex(data[len(data)- 1])[2:]
        crc_orig = crc1 + crc2

        # Contar qunatos CRCs deram errado e nao fazer nada com a mensagem
        if crc_calc != crc_orig:
            print('DEU MERDA NO CRC')
            cntcrc += 1

        #Para os que deram certo

        else:
            v1x = hxm.Extrair_Msg(data,16,17)
            v1y = hxm.Extrair_Msg(data,18,19)
            v2x = hxm.Extrair_Msg(data,20,21)
            v2y = hxm.Extrair_Msg(data,22,23)
            v3x = hxm.Extrair_Msg(data,24,25)
            v3y = hxm.Extrair_Msg(data,26,27)

            dynamic_data_entry(v1x,v2x,v3x,v1y,v2y,v3y)
        # incrementando contadores
        i += 1
        j += 1
        cdata += 1

        if i == 60:
            i = 0
            print('RECEBI 60:   ', j)

        if cdata == 600:
            conn.commit()
            cdata = 0

        if j == maxrecebe:
            tf = time.time()
            break

    s.close()
    timediff = tf - ti
    print('Tempo que o processo levou: ', timediff)




if __name__ == '__main__':
    Main()
