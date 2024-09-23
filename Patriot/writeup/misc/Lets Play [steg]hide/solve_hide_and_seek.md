-> We got `qr_mosaic.bmp`

-> We understand we got to use `steghide` and `stegseek` to extract somefile 

-> steghide is useful to hide and extract file from and image with or without password, and stegseek is to bruteforce the passwod using a wordlist

-> Using steghide on qr_mosaic.bmp, we got an image patriotCTF.bmp saying `patriot ctf`

-> we try to extract image from this one using steghide but it asks for a password. spoiler : bruteforce with stegseek and rockyou doesn't work.

-> I scanned a qr codes from the qr_mosaic.bmp with my phone for the lol and it looked a gibberish but a gibberish that could be a password

-> so i tried to extract all qr codes, using my coder skills (googling) and multiple scripts didn't work

-> [this one](https://note.nkmk.me/en/python-opencv-qrcode/), [this one](https://ctfshellclub.github.io/2019/05/13/ecsc-qrcode/) but it is interesting though, talking about a method which is to slice the qr and read them one by one, until I reached a post (but i forgor the link) (:skull:) talking about a python ai powered qr code reader: [qreader](https://pypi.org/project/qreader/)

-> I try to read one qr code (i sliced the mosaic with [image_slicer](https://github.com/samdobson/image_slicer)  and exported it in PNG installed in a venv through git clone and setup.py install), but it failied...


```
Here the script to read:

from qreader import QReader

import cv2
import sys

path = sys.argv[1]

# Create a QReader instance
qreader = QReader()

# Get the image that contains the QR code
image = cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2RGB)

# Use the detect_and_decode function to get the decoded QR data
decoded_text = qreader.detect_and_decode(image=image)

print(decoded_text)
```
read_one.py

-> THEN ! i got an idea to turn the image in black and white, and it read it ! 

```bash
# python read_one_qr.py slices/qr_mosaic_BW_01_01.png
('C5Nre0R8Tau6T',)
```
-> BTW, i sliced the images with this command : `slice-image qr_mosaic.bmp -r 25 -c 40 -d slices` (i've got 25 by counting the row, and 40 by counting the column all by raw man labor !)

-> Next, i decided to wrote a script that read all sliced qrcode (which are now in `slices/` dir), and wrote every candidate password in a `wordlist.txt` file

```python
from qreader import QReader
from tqdm import tqdm

import os
import cv2
import sys


try:
path = sys.argv[1]
except:
print("usage : extract_passowrds.py <dir>")
sys.exit(0)

qr_list = os.listdir(path)
print(qr_list)

total_qr = len(qr_list)
qr_count = 0
failed_qrs = []

wordlist = []

# Create a QReader instance
qreader = QReader()

for qr in tqdm(qr_list):
    # Get the image that contains the QR code
    image = cv2.cvtColor(cv2.imread(path+qr), cv2.COLOR_BGR2RGB)

    # Use the detect_and_decode function to get the decoded QR data
    decoded_text = qreader.detect_and_decode(image=image)
    #print(f"[+] Decoded qrcode : {decoded_text} from {qr}")

    if not decoded_text:
        failed_qrs.append(qr)
        print(f"failed :{qr} ")
    else:
        wordlist+= decoded_text
        qr_count += 0

print(f"Decoded {qr_count} QR out of total_qr")
"""
with open("wordlist.txt", "w") as f:
    for text in wordlist:
        f.write(text+"\n")

"""
with open("failed.txt", "w") as f:
    for text in failed_qrs:
        f.write(text+"\n")

print(f"Failed {len(failed_qrs)} qrcodes : {failed_qrs} writtent to failed.txt")

print(f"passwords have been written in wordlist.txt")
```

I got a list of about 900 passwords !

-> Then i bruteforce patriot.bmp with the new wordlist

```bash
$ stegseek --crack patriotCTF.bmp --wordlist wordlist.txt

StegSeek 0.6 - https://github.com/RickdeJager/StegSeek

[i] Found passphrase: "hD72ifj7tE83n"
[i] Original filename: "flag_qr_code.bmp".
[i] Extracting to "patriotCTF.bmp.out".
```

-> Then i got a code QR, i read the flag : `PCTF{QR_M0s41c_St3g0_M4st3r}`

