import numpy as np
# from keras.preprocessing import image
import keras.utils as imageutils
import pandas as pd
from keras_facenet import FaceNet

# Reading previously saved csv files contained directory and label
data = pd.read_csv("train_faces_25frames.csv")

images = data["images_list"]
labels = data["label"]

train_data = []
train_label = []
count = 0

embedder = FaceNet()

for (img_path, label) in zip(images, labels):
    img = imageutils.load_img(img_path)
    x = imageutils.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    embeddings = embedder.embeddings(x)
    train_data.append(embeddings)
    # train_label += [label.argmax(1)]
    train_label.append(label)

    if count % 100 == 0:
        print("Number of files done:", count)
    count += 1

train_data = np.array(train_data)
train_label = np.array(train_label)

np.save("train_data_facenet_embeddings.npy", train_data)
np.save("train_label_facenet_embeddings.npy", train_label)
print("All data successfully embedded!")
print("Files saved...")

# Testing part
# for i in images[:5]:
# 	x = i
# 	print(x.shape)
# 	embs = embedder.embeddings(x)
# 	print(embs.shape)
# 	train_data.append(embs)
# 	if count%10==0:
# 		print("Number of files done:", count)
# 	count+=1
