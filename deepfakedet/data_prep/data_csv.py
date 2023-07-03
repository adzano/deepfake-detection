import pandas as pd
import glob
import os
from os.path import isfile, join, split
from os import rename, listdir,  rename, makedirs
from random import shuffle

abs_path = os.path.abspath(os.getcwd())
train_path = ["../train_face/0", "../train_face/1"]

list_1 = [join(train_path[0], x) for x in listdir(train_path[0])]
list_0 = [join(train_path[1], x) for x in listdir(train_path[1])]

c = 0

vid_list = list_1 + list_0
print(len(vid_list))
shuffle(vid_list)

images = []
labels = []

counter = 0
for x in vid_list:
	img = glob.glob(join(abs_path, x, '*.jpg'))
	img.sort(key=lambda f:int(''.join(filter(str.isdigit, f))))
	images+=img[:25]
	label = [k.split('/')[-3] for k in img]
	labels+=label[:25]

	if counter%100==0:
		print("Number of files done:", counter)
	counter+=1

# print(images)
# print(labels)

data = {
	'images_list': images,
	'label': labels
	}

df = pd.DataFrame(data)
df.to_csv("train_faces_25frames.csv", index=False)