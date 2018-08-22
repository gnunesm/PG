from PIL import Image
import os
 
images_path = '/home/gabriel/Documents/PG/MITOS dataset/images/'
cropped_path = '/home/gabriel/Documents/PG/MITOS dataset/cropped_hamamatsu/'

img_list = os.listdir(images_path)
for filename in img_list:
    if 'H' in filename:
        img = Image.open(images_path + filename)
        img = img.crop((0, 0, 1539, 1376))
        img.save(cropped_path + filename)
