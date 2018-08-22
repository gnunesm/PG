import cv2
import os
import numpy as np
import pickle

PATH = '/media/gabriel/Acer/Users/gabri/Documents/PG/'

dataset = {
    'train_data': [],
    'train_labels': [],
    'test_data': [],
    'test_labels': []
}

im_list_train = os.listdir(PATH + 'train/')
im_list_test = os.listdir(PATH + 'test/')

train_idx = 0
test_idx = 0
train_length = len(im_list_train)
test_length = len(im_list_test)

while train_idx < train_length:
    for _ in range(7):
        if train_idx < train_length:
            im_train = im_list_train[train_idx]
            img = cv2.imread(PATH + 'train/' + im_train)
            dataset['train_data'].append(img)
            name = im_train.split('.')[0]
            label = int(name.split('_')[-1])
            dataset['train_labels'].append(label)
            train_idx += 1
    for _ in range(3):
        if test_idx < test_length:
            im_test = im_list_test[test_idx]
            img = cv2.imread(PATH + 'test/' + im_test)
            dataset['test_data'].append(img)
            name = im_test.split('.')[0]
            label = int(name.split('_')[-1])
            dataset['test_labels'].append(label)
            test_idx += 1

    if (train_idx + 1) % 1000 == 0:
        with open('dataset_patch_100_100.pkl', 'wb') as handle:
            pickle.dump(dataset, handle, protocol=pickle.HIGHEST_PROTOCOL)
    print(train_idx + 1, 'images appended from train.')

    
        

