from PIL import Image
import os
 
images_path = '/home/gabriel/Documents/PG/MITOS dataset/cropped_all/'
shrunken_path = '/home/gabriel/Documents/PG/MITOS dataset/shrunken_images/'

basewidth = 32

img_list = os.listdir(images_path)
for filename in img_list:
    img = Image.open(images_path + filename)
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    img.save(shrunken_path + filename)
