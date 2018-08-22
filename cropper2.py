from PIL import Image
import os
 
images_path = '/home/gabriel/Documents/PG/MITOS dataset/shrunken_images/'
cropped_path = '/home/gabriel/Documents/PG/MITOS dataset/cropped_all/'

img_list = os.listdir(images_path)
for filename in img_list:
    if 'tiff' in filename:
        img = Image.open(images_path + filename)
        img = img.crop((0, 0, 357, 357))
        img.save(cropped_path + filename)
