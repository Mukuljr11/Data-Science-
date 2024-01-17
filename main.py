import numpy as np
import qrcode
destination='https://www.instagram.com/'
qr=qrcode.QRCode(version=1,box_size=8,border=6)
qr.add_data(destination)
qr.make()
print("The Shape of this QRCode :",np.array(qr.get_matrix()).shape)
img=qr.make_image(fill_color="black",back_color="white")
img.save("intsaqrcode.png")