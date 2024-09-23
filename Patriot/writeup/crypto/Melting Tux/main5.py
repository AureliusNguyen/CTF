from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
import os
from datetime import datetime
import random

# safe key, trust
key = '00000000000000000000000000000000' 

offset = 15633

def encrypt(raw):
    raw = pad(raw,16)
    cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    return cipher.encrypt(raw)

def decrypt(enc):
    cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    return cipher.decrypt(enc)

flag = open('melting.png', 'rb').read()
assert len(flag) % 16 == 0
chunks = [flag[i*16:i*16+16] for i in range(len(flag)//16)]

a, chunks = chunks[:-offset], chunks[-offset:]

chunks = [decrypt(i) for i in chunks]
open(f'melting{offset}.png', 'wb').write(b"".join(a + chunks))