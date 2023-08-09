import pandas as pd
import numpy as np
import glob
import os
from os.path import isfile, join, split
from os import rename, listdir,  rename, makedirs
from random import shuffle

def maketestlist(real_video, fake_video, num_videos_per_directory=25):
    abs_path = os.path.abspath(os.getcwd())
    eval_path = [os.path.normpath(fake_video), os.path.normpath(real_video)]

    # Function to get all video files from a directory
    def get_video_files(directory):
        video_files = [join(directory, file) for file in os.listdir(directory) if file.endswith('.mp4')]
        return video_files

    list_0 = get_video_files(eval_path[0])
    list_1 = get_video_files(eval_path[1])

    # c = 0
    vid_list = list_1 + list_0
    print("Total number of videos:", len(vid_list))
    shuffle(vid_list)

    videos_list = []
    labels = []
    counter = 0

    for video_file in vid_list:
        videos_list.append(video_file)
        label = 1 if video_file in list_1 else 0
        labels.append(label)
        if counter % 10 == 0:
            print("Number of videos processed:", counter)
        counter += 1

        if counter == num_videos_per_directory:
            break
    
    print("Total Number of videos processed:", counter)
    data = {
        'vids_list': videos_list,
        'label': labels
    }
    df = pd.DataFrame(data)
    df.to_csv("test_vids_label.csv", index=False)
    print(f"All video successfully saved to .CSV with a total of {counter} files.")

    true_labels = np.array(labels)
    np.save("test_labels.npy", true_labels)
    print("All video labels successfully saved")
    print("Files saved...")


real_video = ("./datasets/original_sequences/youtube/c23/videos")
fake_video = ("./datasets/manipulated_sequences/FaceSwap/c23/videos")
maketestlist(real_video, fake_video, num_videos_per_directory=10)