import numpy as np
import cv2
import os

images_path = '/home/gabriel/Documents/PG/MITOS dataset/shrunken_images/'

img_list = os.listdir(images_path)

images = np.empty((594, 3, 357, 400), dtype=np.uint8)
labels = np.empty((594), dtype=np.uint8)

for i, image in enumerate(img_list):
    img = cv2.imread(images_path + image)
    images[i] = img.transpose(2, 0, 1)
    name = image.split('.')[0]
    labels[i] = name.split('_')[-1]
    print(i, image)

print(images.shape)
print(labels)
