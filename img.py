#abc
# from pytesser import *
import pytesseract
from PIL import Image
image = Image.open('8.png')
# image.show()
print(pytesseract.image_to_string(image))
# from PIL import Image
# im = Image.open('C:\\Program Files\\Python37\\Lib\\site-packages\\pytesser3\\timg.jpg')
# print(image_to_string(im))