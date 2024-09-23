from PIL import Image

def extract_lsb(image_path):
    # Open the image
    img = Image.open(image_path)
    
    # Convert image to RGB if it's not in RGB mode
    img = img.convert("RGB")
    
    width, height = img.size
    lsb_list = []

    # Loop through each pixel in the image
    for y in range(height):
        for x in range(width):
            r, g, b = img.getpixel((x, y))

            # Extract the LSB of each color channel
            lsb_r = r & 1
            lsb_g = g & 1
            lsb_b = b & 1

            # Combine the LSBs of RGB channels (if needed) or use just one
            lsb_list.append(lsb_r)
            lsb_list.append(lsb_g)
            lsb_list.append(lsb_b)
    
    # Join the bits and return as a binary sequence (string)
    return ''.join(map(str, lsb_list))

def binary_to_text(binary_sequence):
    # Ensure the binary sequence length is a multiple of 8
    n = 8
    chunks = [binary_sequence[i:i + n] for i in range(0, len(binary_sequence), n)]
    
    # Convert each 8-bit chunk into a character
    text = ""
    for chunk in chunks:
        if len(chunk) == 8:  # Ensure it's a full byte
            decimal_value = int(chunk, 2)  # Convert binary to decimal
            text += chr(decimal_value)  # Convert decimal to ASCII character

    return text

# Example usage
image_path = "img.webp"  # Change to your image path
lsb_data = extract_lsb(image_path)
print(lsb_data)


# Convert the binary LSB sequence into plain text
plain_text = binary_to_text(lsb_data)
print(plain_text)
