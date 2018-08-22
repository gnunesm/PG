import cv2
import os
import numpy as np
# from sklearn.feature_extraction import image

# source path
src_path = '/home/gabriel/Documents/PG/MITOS dataset/images/'

# destination path
dest_path = '/media/gabriel/Acer/Users/gabri/Meus Documentos/PG/'

im_list = os.listdir(src_path)

l1 = 0
l2 = 0
l3 = 0

for im in im_list:
    name = im.split('.')[0]
    part1, part2, label = name.split('_')
    original_name = part1 + '_' + part2
    img = cv2.imread(src_path + im)

    if label == '1':
        if l1 < 32:
            folder_name = 'train/'
            l1 += 1
        else:
            folder_name = 'test/'
    elif label == '2':
        if l2 < 310:
            folder_name = 'train/'
            l2 += 1
        else:
            folder_name = 'test/'
    elif label == '3':
        if l3 < 72:
            folder_name = 'train/'
            l3 += 1
        else:
            folder_name = 'test/'

    number = 0
    i = 0
    while i + 100 <= img.shape[0]:
        j = 0
        while j + 100 <= img.shape[1]:
            patch = img[i:i + 100, j:j + 100]
            cv2.imwrite(dest_path + folder_name + part1 + '_' + part2 + '_' + str(number) + '_' + label + '.tiff', patch)
            number += 1
            j += 100
        i += 100



    # patches = image.extract_patches_2d(img, (100, 100))