from Crypto.Util.number import long_to_bytes

def xor(a, b):
    result = bytearray()
    for x, y in zip(a, b):
        result.append(x ^ y)
    return bytes(result)

def decrypt(encrypted_hex):
    key = 0xadbeefdeadbeefdeadbeef00
    iv = 0
    decrypted = b''
    
    chunks = [encrypted_hex[i:i+32] for i in range(0, len(encrypted_hex), 32)]
    
    for chunk in chunks:
        iv = (iv + 1) % 255
        curr_k = key + iv
        enc = int(chunk, 16)
        decoded = enc ^ curr_k
        decrypted += long_to_bytes(decoded)
    
    return decrypted

with open("out.txt", "r") as file:
    encrypted = file.read().strip()

decrypted = decrypt(encrypted)
msg = [decrypted[i:i+16] for i in range(0, len(decrypted), 16)]


flag = b''
for i in range(0,len(decrypted)//16):
    flag += xor(msg[i], b'\x00\x00\x00\x00\x03s\xa4\xcd=\xfb\xcc4\xc4\x04\x11\x00')

print(flag.decode())