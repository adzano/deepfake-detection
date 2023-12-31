import os

from os.path import isfile, join
from os import rename, listdir, rename, makedirs
from shutil import copyfile

source_folder_1 = './datasets/original_sequences/youtube/c23/videos'
source_folder_2 = './datasets/manipulated_sequences/Deepfakes/c23/videos'
dest_folder_1 = './datasets/train1/1'
dest_folder_2 = './datasets/train1/0'
dest_folder_3 = './datasets/test/1'
dest_folder_4 = './datasets/test/0'

train = 500 # Jumlah Video Untuk Training dalam Setiap Subset
test = 100 # Jumlah Video Untuk Testing
sumtest = train + test

for i, j in zip(listdir(source_folder_1)[:train], listdir(source_folder_2)[:train]):
    copyfile(join(source_folder_1, i), join(dest_folder_1, i))
    copyfile(join(source_folder_2, j), join(dest_folder_2, j))

for i, j in zip(listdir(source_folder_1)[train:sumtest], listdir(source_folder_2)[train:sumtest]):
    copyfile(join(source_folder_1, i), join(dest_folder_3, i))
    copyfile(join(source_folder_2, j), join(dest_folder_4, j))