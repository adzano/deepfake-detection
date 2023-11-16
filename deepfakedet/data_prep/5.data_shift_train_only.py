import os
from os import listdir
from os.path import join
from shutil import copyfile

# Source folders
source_folder_1 = './datasets/original_sequences/youtube/c23/videos'
source_folder_2 = './datasets/manipulated_sequences/Deepfakes/c23/videos'

# Destination folders for testing
dest_folder_3 = './datasets/test1/1'
dest_folder_4 = './datasets/test1/0'

# Define the range for testing data
test_start = 600  # Start from the 500th data
test_end = 700    # End at the 600th data

# Copy files for testing
for i, j in zip(listdir(source_folder_1)[test_start:test_end], listdir(source_folder_2)[test_start:test_end]):
    copyfile(join(source_folder_1, i), join(dest_folder_3, i))
    copyfile(join(source_folder_2, j), join(dest_folder_4, j))
