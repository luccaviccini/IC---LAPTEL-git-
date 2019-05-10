import numpy as np
import matplotlib.pyplot as plt

def car2pol(x,y):
    radius = np.hypot(x,y)

    theta = np.arctan2(y,x)
    return theta, radius

def compass(u, v, arrowprops = None):
    angles, radii = car2pol(u,v)

    fig, ax = plt.subplots(subplot_kw=dict(polar=True))

    kw = []
    kw.append (dict(arrowstyle = "fancy",color = 'green', linewidth = '2',))
    kw.append (dict(arrowstyle = "fancy",color = 'blue', linewidth = '2'))
    kw.append (dict(arrowstyle = "fancy",color = 'red', linewidth = '2'))


    if arrowprops:
        kw.update(arrowprops)
    [ax.annotate("", xy=(angle,radius), xytext=(0,0),arrowprops=w) for angle, radius, w,  in zip(angles,radii, kw)]

    ax.set_ylim(0, np.max(radii))
    plt.title('VA -> Verde;')



    return fig, ax

def twos_complement(hexstr,bits):
     value = int(hexstr,16)
     if value & (1 << (bits-1)):
         value -= 1 << bits
     return value

def Extrair_Msg(byte1,byte2):
    byte1 = hex(test[byte1])[2:]
    byte2 = hex(test[byte2])[2:]
    vx = byte1 + byte2
    x = twos_complement(vx,16)
    return x

test = b'\xaa\x01\x00\x34\x1e\x36\x44\x85\x36\x00\x00\x00\x41\xb1\x00\x00\x39\x2b\x00\x00\xe3\x6a\xce\x7c\xe3\x6a\x31\x83\x04\x44\x00\x00\x09\xc4\x00\x00\x42\xc8\x00\x00\x44\x7a\x00\x00\x46\x1c\x40\x00\x3c\x12\xd4\x3f'


v1x = Extrair_Msg(16,17)
print(v1x)
v1y = Extrair_Msg(18,19)
print(v1y)
v2x = Extrair_Msg(20,21)
print(v2x)
#print(v2x)
v2y = Extrair_Msg(22,23)
print(v2y)
v3x = Extrair_Msg(24,25)
v3y = Extrair_Msg(26,27)


u = [v1x, v2x, v3x]
v = [v1y, v2y, v3y]

t = compass(u,v)
plt.show()
