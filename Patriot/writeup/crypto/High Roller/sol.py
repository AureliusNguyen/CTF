from Crypto.Util.number import *
from Crypto.PublicKey import RSA
import random
import time

pubkey = RSA.import_key(open(".\gen_setup\public_key.pem", "r").read())
c = bytes_to_long(open("flag.enc", "rb").read())
time_i = 1726938600

for i in range(time_i, 1, -1):
    print(time_i - i)
    random.seed(i)
    p, q = getPrime(512, random.randbytes), getPrime(512, random.randbytes)

    if p*q == pubkey.n:
        break

d = pow(pubkey.e, -1, (p-1)*(q-1))
print(long_to_bytes(pow(c, d, pubkey.n)))