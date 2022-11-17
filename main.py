import webbrowser
import qrcode
import qrcode.image.svg

def qr_generator(url):
    img = qrcode.make(url, image_factory=qrcode.image.svg.SvgImage)
    with open('qr.svg', 'wb') as qr:
        img.save(qr)

qr_generator(input("Type the url you want turned into a QR code:\n"))
webbrowser.open("file://C:/Users/benja/Desktop/MakeQRCode/qr.svg")