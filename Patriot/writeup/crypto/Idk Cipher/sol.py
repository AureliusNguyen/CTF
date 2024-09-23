import base64

# The Base64-encoded output from the encoder
encoded_output = "QRVWUFdWEUpdXEVGCF8DVEoYEEIBBlEAE0dQAURFD1I="

# The secret key used in the encoder
srt_key = 'secretkey'

def reverse_encoder(encoded_str, key):
    # Step 1: Base64 Decode
    try:
        decoded_bytes = base64.b64decode(encoded_str)
    except base64.binascii.Error as e:
        print(f"Error decoding Base64: {e}")
        return None

    # Ensure the length of decoded bytes is even
    if len(decoded_bytes) % 2 != 0:
        print("Decoded byte length is not even. Invalid encoding.")
        return None

    half_length = len(decoded_bytes) // 2
    c1_list = []
    c2_list = []

    # Step 2: Split into pairs and XOR with the key
    for i in range(half_length):
        enc_p1 = decoded_bytes[2 * i]
        enc_p2 = decoded_bytes[2 * i + 1]
        key_char = ord(key[i % len(key)])

        # XOR decryption
        c1 = enc_p1 ^ key_char
        c2 = enc_p2 ^ key_char

        # Append decrypted characters
        c1_list.append(chr(c1))
        c2_list.append(chr(c2))

    # Step 3: Reconstruct the original input
    first_half = ''.join(c1_list)
    second_half = ''.join(c2_list)[::-1]  # Reverse the second half

    original_input = first_half + second_half

    return original_input

# Perform the reversal
original_input = reverse_encoder(encoded_output, srt_key)

if original_input:
    # Wrap the flag
    flag = f"pctf{{{original_input}}}"
    print(f"Recovered Flag: {flag}")
else:
    print("Failed to recover the original input.")