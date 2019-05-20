import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D



# Lista com os dados extraído das mensagens. Essa é a parte que os seus códios
# do hex_msg fazem para construir as listas
#listax = [14635, -7318, -7318, 14379, -5782, -7318, 14635, -7318, -7318, 14379, -5782, -7318]
#listay = [0, -12676, 12675, 0, -12676, 12675, 0, -12676, 12675, 0, -12676, 12675]
listax = [5, -2.5, -2.5, 4, -2, -2, 5, -2.5, -2.5, 4, -2, -2]
listay = [0, +4.33, -4.33, 0, +3.46, -3.46, 0, +4.33, -4.33, 0, +3.46, -3.46]
# Essa função estava lá no hex_msg. Coloquei aqui só pra facilitar pra mim, mas
# você pode continuar usando a que estava lá. Inclusive, no cálculo do theta, é
# assim mesmo? com x e y invertidos?
def car2pol (x, y):
    theta = np.arctan2 (y, x)   # E isso mesmo: (y, x)?
    radius = np.hypot (x, y)
    return theta, radius

# Essa é a função de inicialização da animação. Ela vai dizer quais são os
# objetos que serão modificados ao longo do tempo para que o matplotlib possa
# redesenhá-los no gráfico. No nosso caso, esses três objetos (an*) são as 3
# setas, que serão criadas logo abaixo.
def init ():
    return an0, an1, an2

# Essa é a função de animação. Ela é chamada regularmente pelo matplotlib (de
# acordo com o valor definido no paramento interval da FuncAnimation, em
# milisegundos). Essa função faz o seguinte: ela verifica se as duas listas x e
# y possuem o mesmo tamanho e se elas tem ao menos 3 elementos. Se sim, a
# função remove os 3 primeiros elementos da lista, criando as listas internas
# xps e yps. Chama a car2pol para converter as coordenadas e atualiza as setas
# an0, an1 e an2 com as novas posições de x e y. Ao final, ela retorna as 3
# setas, para que a FuncAnimation possa redesenhar esses 3 objetos no gráfico.
def update (num):
    # Somente atualiza as setas se houverem novos elementos na lista
    if len (listax) == len (listay) and len (listax) >= 3:
        # Movendo os 3 primeiros elementos de listax/y para lista x/yps
        xps = listax [:3]
        yps = listay [:3]
        del listax [:3]
        del listay [:3]

        # Convertendo as coordenadas
        angles, radius = car2pol (xps, yps)
        print(radius)
        maxvalue = max(radius)
        print(maxvalue)
        #radius = [x*(1/max) for x in radius]



        #ax.set_ylim (0, np.max(radius))

        # Atualizando as setas com os novos valores
        an0.xy = (angles [0], (radius [0])/maxvalue)
        an1.xy = (angles [1], (radius [1])/maxvalue)
        an2.xy = (angles [2], (radius [2])/maxvalue)

    return an0, an1, an2

# A animação no python funciona assim: você cria uma figura base, que não vai
# ser modificada, e vai criando os objetos (setas, linhas, legendas, etc), que
# podem ser modificados ao longo do tempo. Nesses comandos abaixo a figura base
# está sendo criada. É importante que você defina aqui as escalas do gráfico,
# que não poderão mudar ao longo do tempo.


# criando lista secundaria
'''
for i in listax and j in listay:

    lx2, ly2 = listax [:3], listay [:3]
    theta, radius = car2pol(i, j)
'''


fig, ax = plt.subplots (subplot_kw = dict (polar=True))
ax.set_ylim (0, 1)
plt.title ('Tensoes')

colors = ['green', 'blue', 'red']
lines = [Line2D([0], [0], color=c, linewidth=3) for c in colors]
labels = ['V1', 'V2', 'V3']
plt.legend(lines, labels, loc = 'lower right')
# Aqui estamos criando as setas (anotações), que serão modificadas em tempo
# real. Essa setas estão sendo configuradas em termos de formato uma única vez,
# e nesse primeiro momento elas estão todas nas coordenadas 0,0, por isso você
# não vai vê-las no gráfico. Essas coordenadas serão modificadas pela função
# update ao longo do tmepo.
propslist = []
propslist.append (dict (arrowstyle = "fancy", color = 'green', linewidth = '2'))
propslist.append (dict (arrowstyle = "fancy", color = 'blue', linewidth = '2'))
propslist.append (dict (arrowstyle = "fancy", color = 'red', linewidth = '2'))
an0 = ax.annotate ("", xy = (0, 0), xytext = (0, 0), arrowprops = propslist [0])
an1 = ax.annotate ("", xy = (0, 0), xytext = (0, 0), arrowprops = propslist [1])
an2 = ax.annotate ("", xy = (0, 0), xytext = (0, 0), arrowprops = propslist [2])
'''
red = mpatches.Patch(color='red', label='V1')
blue = mpatches.Patch(color='blue', label='V2')
green = mpatches.Patch(color='green', label='V3')

plt.legend(handles=[red, blue, green], loc = 'lower right')

'''
''''
colors = ['green', 'blue', 'red']
lines = [Line2D([0], [0], color=c, linewidth=3) for c in colors]
labels = ['V1', 'V2', 'V3']
plt.legend(lines, labels, loc = 'lower right')
'''






# Iniciando a animação. Você pode ajustar o interval para que a animação seja mais rápida ou lenta.
anim = animation.FuncAnimation (fig, update, init_func = init, interval = 1000, blit = False)
plt.show ()
