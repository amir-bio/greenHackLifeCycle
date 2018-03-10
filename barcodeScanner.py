from pyzbar.pyzbar import decode
from PIL import Image


results =   decode(Image.open('imageTest2.jpg'))
for result in results:
    print result



