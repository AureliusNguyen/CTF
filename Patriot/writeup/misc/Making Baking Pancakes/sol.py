from pwn import *

# Set up the connection to the server
conn = remote('chal.pctf.competitivecyber.club',  9001)

# Welcome to the pancake shop!
# Pancakes have layers, we need you to get through them all to get our secret pancake mix formula.
# This server will require you to complete 1000 challenge-responses.
# A response can be created by doing the following:
# 1. Base64 decoding the challenge once (will output (encoded|n))
# 2. Decoding the challenge n more times.
# 3. Send (decoded|current challenge iteration)
# Example response for challenge 485/1000: e9208047e544312e6eac685e4e1f7e20|485
# Good luck!

# Challenge: VjIweFNtUXhiSEZaTTJoT1VrZGplRmRyWkU5aGJHeHhXa2RzV2xZeFZqTlhiWEJDVGtac2NWSllhRTVOYTJ0M1ZERlNjMkZHYkZWVFZEQTl8Mw==
# (0/1000) >>
index =0
for i in range(1000):
    conn.recvuntil(b'Challenge: ')

    ct = conn.recvline().strip().decode()
    print(ct)
    # Decode the challenge
    decoded = b64d(ct).decode()
    print(decoded)

    itera = int(decoded.split('|')[1])
    decoded = decoded.split('|')[0]
    
    for i in range(itera):
        decoded = b64d(decoded).decode()
    print(decoded)
    conn.recvuntil(b'>> ')
    print("SENDING: ", decoded.encode() + b'|' + str(index).encode())
    conn.sendline((decoded + '|' + str(index)).encode())
    index += 1
    # print(conn.recvline())
print(conn.recvall())