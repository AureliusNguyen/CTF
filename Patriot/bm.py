import cv2
import numpy as np

# Load the mosaic image
image_path = 'qr_mosaic.bmp'  # Adjust to your file path
image = cv2.imread(image_path)

# Parameters for the size of each QR code
qr_code_width = 92   # Width of each individual QR code (in pixels)
qr_code_height = 36  # Height of each individual QR code (in pixels)

# Get the dimensions of the image
image_height, image_width, _ = image.shape

# Calculate the number of QR codes along the x and y axes
num_qr_codes_x = image_width // qr_code_width
num_qr_codes_y = image_height // qr_code_height

# Initialize a list to hold decoded data
decoded_data = []

# Function to decode a QR code from an image
def decode_qr_code(qr_image):
    detector = cv2.QRCodeDetector()
    data, bbox, _ = detector.detectAndDecode(qr_image)
    
    if bbox is not None:
        return data
    else:
        return None

# Add padding to the QR code image to help with detection
def add_padding(qr_image, padding_size=10):
    return cv2.copyMakeBorder(qr_image, padding_size, padding_size, padding_size, padding_size, cv2.BORDER_CONSTANT, value=[255, 255, 255])

# Loop over each QR code in the mosaic
for i in range(num_qr_codes_x):
    for j in range(num_qr_codes_y):
        try:
            # Define the region of interest (ROI) for each QR code
            x_start = i * qr_code_width
            y_start = j * qr_code_height
            x_end = (i + 1) * qr_code_width
            y_end = (j + 1) * qr_code_height

            # Extract the individual QR code
            qr_code_image = image[y_start:y_end, x_start:x_end]

            # Add padding to the QR code to improve detection
            padded_qr_code_image = add_padding(qr_code_image)

            # Decode the QR code
            data = decode_qr_code(padded_qr_code_image)
            
            if data:
                print(f"Decoded data at position ({i}, {j}): {data}")
                decoded_data.append(data)
            else:
                print(f"No QR code detected at position ({i}, {j})")
        
        except Exception as e:
            print(f"Error decoding QR code at position ({i}, {j}): {e}")

# Combine the decoded data
full_message = ''.join(decoded_data)
print(f"Full decoded message: {full_message}")
