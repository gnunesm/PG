import cv2
import os
import numpy as np
import pickle

# ../input/
PATH = '/home/gabriel/Documents/PG/MITOS dataset/images/'

#new_width = 100
#new_heigth = 100
new_dim = 100

im_list = os.listdir(PATH)
dataset = {
    'data': [],
    'labels': []
}

for im in im_list:
    img = cv2.imread(PATH + im)
    height = img.shape[0]
    img = img[:, :height, :]
    img = cv2.resize(img, (new_dim, new_dim), interpolation=cv2.INTER_CUBIC)
    dataset['data'].append(img)
    name = im.split('.')[0]
    label = name.split('_')[-1]
    dataset['labels'].append(label)

with open('dataset.pkl', 'wb') as handle:
    pickle.dump(dataset, handle, protocol=pickle.HIGHEST_PROTOCOL)