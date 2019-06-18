'''
            if cntplot == 20:
                cntplot = 0
                # extraindo os valores de tensao da mensagem e colocando em duas listas.
                listax = []
                listay = []

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
