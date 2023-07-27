import pandas as pd
import numpy as np
import glob
import os
from os.path import isfile, join, split
from os import rename, listdir,  rename, makedirs
from random import shuffle

def maketestlist(real_video, fake_video, num_videos_per_directory):
    abs_path = os.path.abspath(os.getcwd())
    eval_path = [os.path.normpath(fake_video), os.path.normpath(real_video)]

    # Function to get all video files from a directory and its subdirectories
    def get_video_files(directory):
        video_files = []
        for root, dirs, files in os.walk(directory):
            video_files.extend([os.path.join(root, file) for file in files if file.endswith('.mp4')])
        return video_files

    list_1 = get_video_files(eval_path[0])
    list_0 = get_video_files(eval_path[1])

    c = 0
    vid_list = list_1 + list_0
    print("Total number of videos:", len(vid_list))
    shuffle(vid_list)

    videos_list = []
    labels = []
    counter = 0

    for x in vid_list:
        vid = glob.glob(join(abs_path, x))
        videos_list += vid[:num_videos_per_directory]
        label = [os.path.basename(os.path.dirname(os.path.dirname(k))) for k in vid]
        labels += label[:num_videos_per_directory]
        if counter % 10 == 0:
            print("Number of videos processed:", counter)
        counter += 1

    data = {
        'vids_list': videos_list,
        'label': labels
    }
    df = pd.DataFrame(data)
    df.to_csv("test_vids_label.csv", index=False)
    print(f"All video successfully saved to .CSV with a total of {counter} files.")

    true_labels = []
    counterlabel = 0
    for label in labels:
        true_labels.append(label)
        if counterlabel % 10 == 0:
            print("Number of Videos done: ", counterlabel)
        counterlabel += 1

    true_labels = np.array(true_labels)
    np.save("test_labels.npy", true_labels)
    print("All video successfully embedded!")
    print("Files saved...")

real_video = ("./datasets/original_sequences/youtube/c23/videos")
fake_video = ("./datasets/manipulated_sequences/FaceSwap/c23/videos")
maketestlist(real_video, fake_video, num_videos_per_directory=10)