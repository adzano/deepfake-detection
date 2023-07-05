import os

from os.path import isfile, join
from os import rename, listdir, rename, makedirs
from shutil import copyfile

source_folder_1 = './datasets/original_sequences/youtube/c23/videos'
source_folder_2 = './datasets/manipulated_sequences/NeuralTextures/c23/videos'
dest_folder_1 = './datasets/train/1'
dest_folder_2 = './datasets/train/0'
dest_folder_3 = './datasets/test/1'
dest_folder_4 = './datasets/test/0'


for i, j in zip(listdir(source_folder_1)[:100], listdir(source_folder_2)[:100]):
    copyfile(join(source_folder_1, i), join(dest_folder_1, i))
    copyfile(join(source_folder_2, j), join(dest_folder_2, j))

for i, j in zip(listdir(source_folder_1)[100:200], listdir(source_folder_2)[100:200]):
    copyfile(join(source_folder_1, i), join(dest_folder_3, i))
    copyfile(join(source_folder_2, j), join(dest_folder_4, j))