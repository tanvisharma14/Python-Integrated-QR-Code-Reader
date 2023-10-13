# install pyzbar, it has decode functin 
# install pillow, to perform operations on picture

from pyzbar.pyzbar import decode
from PIL import Image

# reading img
img = Image.open("myQr.png")

# decoding img
result = decode(img)

# print content from qr
print(result[0].data.decode())  # result[0] -> img, .data -> to access result's data/return binary or encoded,
                                # .decode -> converts data into string