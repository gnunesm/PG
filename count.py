import os

images_path = '/home/gabriel/Documents/PG/MITOS dataset/images/'

label_1 = 0
label_2 = 0
label_3 = 0

images = os.listdir(images_path)

for im in images:
    if '_1.tiff' in im:
        label_1 += 1
    elif '_2.tiff' in im:
        label_2 += 1
    elif '_3.tiff' in im:
        label_3 += 1

print('Label 1:', label_1)
print('Label 2:', label_2)
print('Label 3:', label_3)