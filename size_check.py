from PIL import Image
import os

img_list = os.listdir()
for filename in img_list:
    if filename != 'size_check.py':
        img = Image.open(filename)
        width, height = img.size
        if width != 400:
            print(filename + ' width = ' + width)
        if height != 357:
            print(filename + ' height = ' + height)