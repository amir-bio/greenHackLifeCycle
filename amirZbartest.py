from PIL import Image

import zbar
import cv2 as cv


# image = cv.imread("t4.jpg")
# cv2_im = cv.cvtColor(image,cv.COLOR_BGR2RGB)
# PILIm = Image.fromarray(cv2_im)
# PILIm.show()

# width, height = PILIm.size
# raw = PILIm.tobytes()
#print type(image) # <type 'numpy.ndarray'>


#image = read_image_into_numpy_array(...) # whatever function you use to read an image file into a numpy array



pil = Image.open("q.jpg").convert('L')
pil.show()

width, height = pil.size
raw = pil.tobytes()


scanner = zbar.ImageScanner()
scanner.parse_config('enable')

zimage = zbar.Image(width, height, 'Y800', raw)

results = scanner.scan(zimage)

for result in results:
    print(result.type, result.data, result.quality, result.position)