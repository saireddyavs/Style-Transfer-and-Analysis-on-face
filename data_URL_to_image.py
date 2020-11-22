print("Hi")
data = open("imagee.txt").read()

from PIL import  Image
import  io, base64


im = Image.open(io.BytesIO(base64.b64decode(data.split(',')[1])))
im.save("static/uploads/image.jpg")
