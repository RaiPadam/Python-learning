import qrcode

qr_text = "sms:<9746283960>?body=<Hello>"

img = qrcode.make(qr_text)
type(img)   # qrcode.image.pil.PilImage
img.save("mobile.png")
print("QR Image Successfully Saved.")
