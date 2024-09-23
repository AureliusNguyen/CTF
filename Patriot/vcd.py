import cv2
import numpy as np

# Load the mosaic image
image_path = 'qr_mosaic.bmp'  # Adjust to your file path
image = cv2.imread(image_path)

# Parameters for the size of each QR code
qr_code_width = 58  # Width of each QR code (58 pixels)
qr_code_height = 58  # Height of each QR code (58 pixels)

# Initialize a list to hold decoded data
decoded_data = []

# Function to decode a QR code from an image
def decode_qr_code(qr_image):
    detector = cv2.QRCodeDetector()
    data, bbox, _ = detector.detectAndDecode(qr_image)
    return data if data else None

# Loop over each QR code in the mosaic
for i in range(40):  # 40 QR codes in width
    for j in range(25):  # 25 QR codes in height
        try:
            # Define the region of interest (ROI) for each QR code
            x_start = i * qr_code_width
            y_start = j * qr_code_height
            x_end = (i + 1) * qr_code_width
            y_end = (j + 1) * qr_code_height

            # Extract the individual QR code
            qr_code_image = image[y_start:y_end, x_start:x_end]

            # Decode the QR code
            data = decode_qr_code(qr_code_image)
            
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


