from tqdm import tqdm

def long_to_bytes(val, endianness='big'):
    width = (val.bit_length() + 7) // 8
    return val.to_bytes(width, byteorder=endianness)

flag = bytes.fromhex("a" * 74)

# Initialize state dictionary
state = {i: [0] * (len(flag) * 7) for i in range(len(flag) + 1)}

# Open output.txt for reading
with open('output.txt', 'r') as f:
    # Process the file in batches (assuming 1,000,000 iterations)
    for i in tqdm(range(1000000)):
        ct = int(f.readline().strip(), 16)  # Read and convert hex to int
        abc = bin(ct)[2:].zfill(len(flag) * 8)  # Convert int to binary and zero-pad to 8 bits
        st = abc[::8].count("1")  # Count the number of "1"s in the binary string

        # Update state
        for i in range(len(flag) * 7):
            state[st][i] += abc[1 + i + i // 7] == "1"

# Reconstruct the bitstring
bitstring = ""
for i in range(len(flag) * 7):
    if i % 7 == 0:
        bitstring += "0"  # Add padding at the start of every 7-bit sequence

    # Use state to determine if the bit should be "1" or "0"
    if sum(state[j][i] <= sum(state[j]) / len(state[j]) for j in range(10, 14)) + sum(state[j][i] >= sum(state[j]) / len(state[j]) for j in range(19, 23)) >= 4:
        bitstring += "1"
    else:
        bitstring += "0"

# Convert the bitstring to bytes and print the result
result_bytes = long_to_bytes(int(bitstring, 2))
print(result_bytes)
