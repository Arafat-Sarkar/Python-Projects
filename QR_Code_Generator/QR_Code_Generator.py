import qrcode

# QR code e  data  (URL / text)
data = "https://github.com/Arafat-Sarkar"

# QRCode object create
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# data add 
qr.add_data(data)

# QR structure generate 
qr.make(fit=True)

# image create
img = qr.make_image(fill_color="black", back_color="white")

# image save
img.save("my_qr.png")

print("QR Code generated successfully!")
