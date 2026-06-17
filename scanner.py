import qrcode as qr
img=qr.make("https://github.com")
img.save("Naisargi.png")
img.show()
#import qrcode
#import os
#
#img = qrcode.make("https://www.youtube.com")
#
#filename = "scanner.png"
#img.save(filename)
#
#print("Saved at:", os.path.abspath(filename))
#
#img.show()