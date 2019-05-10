#import numpy as np
import matplotlib.pyplot as plt
import hex_msg as hxm


test = b'\xaa\x01\x00\x34\x1e\x36\x44\x85\x36\x00\x00\x00\x41\xb1\x00\x00\x39\x2b\x00\x00\xe3\x6a\xce\x7c\xe3\x6a\x31\x83\x04\x44\x00\x00\x09\xc4\x00\x00\x42\xc8\x00\x00\x44\x7a\x00\x00\x46\x1c\x40\x00\x3c\x12\xd4\x3f'


v1x = hxm.Extrair_Msg(test,16,17)
print(v1x)
v1y = hxm.Extrair_Msg(test,18,19)
print(v1y)
v2x = hxm.Extrair_Msg(test,20,21)
print(v2x)
#print(v2x)
v2y = hxm.Extrair_Msg(test,22,23)
print(v2y)
v3x = hxm.Extrair_Msg(test,24,25)
v3y = hxm.Extrair_Msg(test,26,27)


u = [v1x, v2x, v3x]
v = [v1y, v2y, v3y]

t = hxm.compass(u,v)
plt.show()
