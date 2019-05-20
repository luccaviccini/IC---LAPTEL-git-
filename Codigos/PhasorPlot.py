#import numpy as np
import matplotlib.pyplot as plt
import hex_msg as hxm

test2 = b'\xaa\x01\x00\x34\x1e\x36\x44\x85\x36\x00\x00\x00\x41\xb1\x00\x00\x38\x2b\x00\x00\xe9\x6a\xce\x7c\xe3\x6a\x31\x83\x04\x44\x00\x00\x09\xc4\x00\x00\x42\xc8\x00\x00\x44\x7a\x00\x00\x46\x1c\x40\x00\x3c\x12\xd4\x3f'
test = b'\xaa\x01\x00\x34\x1e\x36\x44\x85\x36\x00\x00\x00\x41\xb1\x00\x00\x39\x2b\x00\x00\xe3\x6a\xce\x7c\xe3\x6a\x31\x83\x04\x44\x00\x00\x09\xc4\x00\x00\x42\xc8\x00\x00\x44\x7a\x00\x00\x46\x1c\x40\x00\x3c\x12\xd4\x3f'
listax = []
listay = []



v1x = hxm.Extrair_Msg(test,16,17)
listax.append(v1x)
v1y = hxm.Extrair_Msg(test,18,19)
listay.append(v1y)
v2x = hxm.Extrair_Msg(test,20,21)
listax.append(v2x)
v2y = hxm.Extrair_Msg(test,22,23)
listay.append(v2y)
v3x = hxm.Extrair_Msg(test,24,25)
listax.append(v3x)
v3y = hxm.Extrair_Msg(test,26,27)
listay.append(v3y)

v1x = hxm.Extrair_Msg(test2,16,17)
listax.append(v1x)
v1y = hxm.Extrair_Msg(test2,18,19)
listay.append(v1y)
v2x = hxm.Extrair_Msg(test2,20,21)
listax.append(v2x)
v2y = hxm.Extrair_Msg(test2,22,23)
listay.append(v2y)
v3x = hxm.Extrair_Msg(test2,24,25)
listax.append(v3x)
v3y = hxm.Extrair_Msg(test2,26,27)
listay.append(v3y)



listaxp = []
listayp = []
c = 0
j = 0
print('listax: ', listax)
while listax:
    i = listax.pop(c)
    print('listax: ', listax)
    listaxp.append(i)
    print('listaxp: ', listaxp)
    p = listay.pop(c)
    listayp.append(p)
    c = c + 1
    if c == 3:
        print('entrou')
        print(listaxp, listayp)
        fig, ax = hxm.compass(listaxp,listayp)
        plt.show()
        listaxp.clear()
        listayp.clear()        
        c = 0
    
    
    
    
    

#fig, ax = hxm.compass(listax,listay)
#plt.show()
