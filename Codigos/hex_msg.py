import numpy as np
import matplotlib.pyplot as plt

msg = b'\xaa\x01\x00\x34\x1e\x36\x44\x85\x36\x00\x00\x00\x41\xb1\x00\x00\x39\x2b\x00\x00\xe3\x6a\xce\x7c\xe3\x6a\x31\x83\x04\x44\x00\x00\x09\xc4\x00\x00\x42\xc8\x00\x00\x44\x7a\x00\x00\x46\x1c\x40\x00\x3c\x12\xd4\x3f'


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
    plt.title('Tensoes')
    return fig, ax

def twos_complement(hexstr,bits):
     value = int(hexstr,16)
     if value & (1 << (bits-1)):
         value -= 1 << bits
     return value


#extrai mensagem e concatena com 2 bytes
def Extrair_Msg(msg,byte1,byte2):
    
    zstr = '0'
    
    byte1 = hex(msg[byte1])[2:]
    if len(byte1) == 1:
        zstr += byte1
        byte1 = zstr 
    
    byte2 = hex(msg[byte2])[2:]
    if len(byte2) == 1:
        zstr += byte2
        byte2 = zstr       

    vx = byte1 + byte2    
                
    vx = twos_complement(vx,16)

    return vx


#extrai mensagem e concatena com 3 bytes
def Extrair_Msg3(msg,byte1,byte2,byte3):
    zstr = '0'
    
    byte1 = hex(msg[byte1])[2:]
    
    if len(byte1) == 1:
        zstr += byte1
        byte1 = zstr    
    
    byte2 = hex(msg[byte2])[2:]
    if len(byte2) == 1:
        zstr += byte2
        byte2 = zstr    
    byte3 = hex(msg[byte3])[2:]
    
    if len(byte3) == 1:
        zstr += byte3
        byte3 = zstr     
    

    vx = byte1 + byte2 + byte3
    
    var = vx[len(vx) - 1]
    if var == '0':
        vx += '0'
     
    vx = twos_complement(vx,16) 
        
    return vx

#extrai mensagem e concatena com 4 bytes
def Extrair_Msg4(msg,byte1,byte2,byte3,byte4):
    zstr = '0'
    
    byte1 = hex(msg[byte1])[2:]
    if len(byte1) == 1:
        zstr += byte1
        byte1 = zstr     
        
    byte2 = hex(msg[byte2])[2:]   
    if len(byte2) == 1:
        zstr += byte2
        byte2 = zstr     
        
    byte3 = hex(msg[byte3])[2:] 
    if len(byte3) == 1:
        zstr += byte3
        byte3 = zstr 
        
    byte4 = hex(msg[byte4])[2:]
    if len(byte4) == 1:
        zstr += byte4
        byte4 = zstr 
   
    vx = byte1 + byte2 + byte3 + byte4
    var = vx[len(vx) - 1]
       
    
    vx = twos_complement(vx,16)

    return vx


p = Extrair_Msg(msg,22,23)
print(p)
