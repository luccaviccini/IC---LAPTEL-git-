test = b'\xaa\x01\x00\x34\x1e\x36\x44\x85\x36\x00\x00\x00\x41\xb1\x00\x00\x39\x2b\x00\x00\xe3\x6a\xce\x7c\xe3\x6a\x31\x83\x04\x44\x00\x00\x09\xc4\x00\x00\x42\xc8\x00\x00\x44\x7a\x00\x00\x46\x1c\x40\x00\x3c\x12\xd4\x3f'
v = hex(test[16])[2:]
u = hex(test[17])[2:]



w = v + u

print(w)
i = int(w,16)
print(i)
