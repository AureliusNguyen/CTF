import base64

# The XOR key provided in the Base64 encoded form
srt_key_base64 = 'QRVWUFdWEUpdXEVGCF8DVEoYEEIBBlEAE0dQAURFD1I='

# Decode the key from Base64
srt_key = base64.b64decode(srt_key_base64).decode()

# Example Base64 encoded string (replace this with the actual output from the program)
b64_enc_val = input("Enter Base64 Encoded Value: ")

# Add padding if the length is not divisible by 4
missing_padding = len(b64_enc_val) % 4
if missing_padding != 0:
    b64_enc_val += '=' * (4 - missing_padding)

# Now, decode the Base64 string
encoded_val = base64.b64decode(b64_enc_val).decode()

# Since the script XORs both forward and reverse input characters, we will undo it.
output_arr = list(encoded_val)
usr_input = []

# The process needs to be reversed:
for i in range(0, len(output_arr), 2):
    enc_p1 = output_arr[i]
    enc_p2 = output_arr[i + 1]

    # Reverse the XOR operation
    c1 = chr(ord(enc_p1) ^ ord(srt_key[i // 2 % len(srt_key)]))
    c2 = chr(ord(enc_p2) ^ ord(srt_key[i // 2 % len(srt_key)]))

    usr_input.append(c1)
    usr_input.insert(0, c2)  # Rebuild the original string from reverse

# Join the list to form the original input
original_input = ''.join(usr_input)
print(f"Original input was: {original_input}")
