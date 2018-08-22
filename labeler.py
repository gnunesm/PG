import os
import csv

train_numbers = ['03', '04', '05', '07', '10', '11', '12', '14', '15', '17', '18']


images_path = '/home/gabriel/Documents/PG/MITOS dataset/images/'

for number in train_numbers:
    path = '/home/gabriel/Documents/PG/MITOS dataset/training_hamamatsu/H' + number + '/atypia/x20/'
    csv_list = os.listdir(path)
    for name in csv_list:
        if 'decision' in name:
            parts = name.split('_')
            image_name = parts[0] + '_' + parts[1]
            with open(path + name) as csvfile:
                readCSV = csv.reader(csvfile, delimiter=',')
                score = [row[0] for row in readCSV]                 # it's a list
                try:
                    os.rename(images_path + image_name + '.tiff', images_path + image_name + '_' + score[0] + '.tiff')
                except FileNotFoundError:
                    print(image_name + ' had already been renamed.')
                    pass
                except IndexError:
                    print(image_name + ' has some problem on its label.')
