# List of hex values from the image
hex_values = [
    "52", "41", "56", "44", "79", "4a", "42", "70", "66", "5d", "47", "6c", "61",
    "70", "7b", "72", "76", "6b", "6d", "6c", "5d", "6b", "71", "5d", "31", "63", 
    "71", "7b"
]

# Convert hex to ASCII
ascii_values = ''.join([chr(int(hv, 16)) for hv in hex_values])
print(ascii_values)

def enc(din):
    temp = (din & 0x3FF)
    temp = temp << 2
    temp = temp ^ 0xA
    dout = (temp >> 2)
    dout = dout & 0xFF
    return dout

ciph = b"RAVDyJBpf]Glap{rvkml]kq]1cq{"

for x in ciph:
    for i in range(255):
        if enc(i) == x:
            print(chr(i), end="")