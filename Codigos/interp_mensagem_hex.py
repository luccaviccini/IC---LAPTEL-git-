test = b'\xaa\x01\x00\x34\x1e\x36\x44\x85\x36\x00\x00\x00\x41\xb1\x00\x00\x39\x2b\x00\x00\xe3\x6a\xce\x7c\xe3\x6a\x31\x83\x04\x44\x00\x00\x09\xc4\x00\x00\x42\xc8\x00\x00\x44\x7a\x00\x00\x46\x1c\x40\x00\x3c\x12\xd4\x3f'

def twos_complement(hexstr,bits):
     value = int(hexstr,16)
     if value & (1 << (bits-1)):
         value -= 1 << bits
     return value


def Extrair_Msg(byte1,byte2):
    byte1 = hex(test[byte1])[2:]
    byte2 = hex(test[byte2])[2:]

    vx = byte1 + byte2
    vx = twos_complement(vx,16)

    return vx


x = Extrair_Msg(20,21)
print(x)
y = Extrair_Msg(22,23)
print(y)
'''
import numpy as np
s = '392b'
s2 = '0000'
def twos_complement(hexstr,bits):
     value = int(hexstr,16)
     if value & (1 << (bits-1)):
         value -= 1 << bits
     return value



print(twos_complement(s,16))
print(twos_complement(s2,16))


'''
#lista = []
#ista.append((x,y))
