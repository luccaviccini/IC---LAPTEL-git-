import socket
import time
import matplotlib.animation as animation
import crc_calculation as C
import hex_msg as hxm
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import matplotlib.patches as mpatches

def Parametros(): ## Parametros a serem definidos antes do inicio do codigo

    server_ip = '10.15.1.22'
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
    cntcrc = 0
    cntplot = 1
    data = None
    print('Server Started. ')


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
            cntcrc = cntcrc + 1

        #Para os que deram certo

        else:
            if cntplot == 20:
                cntplot = 0
                # extraindo os valores de tensao da mensagem e colocando em duas listas.
                listax = []
                listay = []

                v1x = hxm.Extrair_Msg(data,16,17)
                v1y = hxm.Extrair_Msg(data,18,19)
                v2x = hxm.Extrair_Msg(data,20,21)
                v2y = hxm.Extrair_Msg(data,22,23)
                v3x = hxm.Extrair_Msg(data,24,25)
                v3y = hxm.Extrair_Msg(data,26,27)
                listax.append(v1x)
                listay.append(v1y)
                listax.append(v2x)
                listay.append(v2y)
                listax.append(v3x)
                listay.append(v3y)

                def init():
                    return an0, an1, an2

                def update (num):

    # Somente atualiza as setas se houverem novos elementos na lista

                    if len (listax) == len (listay) and len (listax) >= 3:

                        # Movendo os 3 primeiros elementos de listax/y para lista x/yps
                        xps = listax [:3]
                        yps = listay [:3]
                        del listax [:3]
                        del listay [:3]
                        # Convertendo as coordenadas
                        angles, radius = hxm.car2pol (xps, yps)
                        maxvalue = max(radius)
                        # Atualizando as setas com os novos valores
                        an0.xy = (angles [0], (radius [0])/maxvalue)
                        an1.xy = (angles [1], (radius [1])/maxvalue)
                        an2.xy = (angles [2], (radius [2])/maxvalue)

                        return an0, an1, an2

                # propriedades do gráfico
                fig, ax = plt.subplots (subplot_kw = dict (polar=True))
                ax.set_ylim (0, 1) # limite do raio do grafico polar
                plt.title ('Tensoes')
                colors = ['green', 'blue', 'red']
                lines = [Line2D([0], [0], color=c, linewidth=3) for c in colors]
                labels = ['V1', 'V2', 'V3']
                plt.legend(lines, labels, loc = 'lower right')

                propslist = []

                propslist.append (dict (arrowstyle = "fancy", color = 'green', linewidth = '2'))
                propslist.append (dict (arrowstyle = "fancy", color = 'blue', linewidth = '2'))
                propslist.append (dict (arrowstyle = "fancy", color = 'red', linewidth = '2'))
                an0 = ax.annotate ("", xy = (0, 0), xytext = (0, 0), arrowprops = propslist [0])
                an1 = ax.annotate ("", xy = (0, 0), xytext = (0, 0), arrowprops = propslist [1])
                an2 = ax.annotate ("", xy = (0, 0), xytext = (0, 0), arrowprops = propslist [2])

                anim = animation.FuncAnimation (fig, update, init_func = init, interval = 1000, blit = False)

                plt.show ()





        cntplot = cntplot + 1
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
