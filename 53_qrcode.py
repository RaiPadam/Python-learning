import qrcode

qr_text = "Padam Rai"
img = qrcode.make(qr_text)
type(img)   # qrcode.image.pil.PilImage
img.save("brp.png")
print("QR Image Successfully Saved.")