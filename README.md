# qrcode_generator
QR code generator using python

What is a QR Code?
A Quick Response code is a two-dimensional pictographic code used for its fast readability and comparatively large storage capacity. The code consists of black modules arranged in a square pattern on a white background. The information encoded can be made up of any kind of data (e.g., binary, alphanumeric, or Kanji symbols)

to install in python-
pip install qrcode

--------------------------------------
import qrcode
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=4,
)
qr.add_data('Some data')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")


The version parameter is an integer from 1 to 40 that controls the size of the QR Code (the smallest, version 1, is a 21x21 matrix).
Set to None and use the fit parameter when making the code to determine this automatically.

fill_color and back_color can change the background and the painting color of the QR, when using the default image factory. 
Both parameters accept RGB color tuples.

The box_size parameter controls how many pixels each “box” of the QR code is.

The border parameter controls how many boxes thick the border should be (the default is 4, which is the minimum according to the specs).

## code--
![image](https://user-images.githubusercontent.com/89141709/189383973-41c96eaa-af12-4a88-a728-f6a9a7b03db7.png)

## qrcode generated--
![image](https://user-images.githubusercontent.com/89141709/189384082-8e351f06-457a-4d92-89b9-3c1334027072.png)

## after scanning it redirect to the page--
![image](https://user-images.githubusercontent.com/89141709/189384201-5c8d53ed-1fdb-45dc-8842-dd9eb24ca193.png)
