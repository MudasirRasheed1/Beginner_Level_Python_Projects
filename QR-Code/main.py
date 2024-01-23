import qrcode


def Qr_code():
    data = input("Enter the data to be encoded: ")
    qr = qrcode.QRCode(version=1, box_size=10, border=5) #Using QRCode class from qrcode module
    qr.add_data(data) #Adding data to the QRCode
    qr.make(fit=True) #Generating the QRCode
    img = qr.make_image(fill="black", back_color="white") #Making the image of the QRCode, object of type image is returned
    img.show()
    print("QR-Code Generated")


if __name__ == "__main__":
    print("Welcome to QR-Code Generator")
    Qr_code()


