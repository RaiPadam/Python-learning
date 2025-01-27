
import qrcode
img = qrcode.make('Tilkeni Basic School')
type(img)  # qrcode.image.pil.PilImage
img.save("my_school.png")
print("QR Image Successfully Saved")