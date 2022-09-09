import qrcode
import image

qr=qrcode.QRCode(
    version=15,  #15 means the version of the qr code high the number bigger the code image and complicated picture
    box_size=10, # size of the box where qr code will be displayed
    border=5  #it is the white part of image ---border in all 4 sides with white color
)

data="https://portfolio-ashutosh.netlify.app/"
# it will redirect to the portfolio website after scanning qrcode.

qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="black",back_color="white")
img.save("qr.png")