import cv2
import os

def extract_frames(video_path, output_folder, num_frames):
    # Open the video file
    video = cv2.VideoCapture(video_path)

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get the total number of frames in the video
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

    # Calculate the indices of frames to extract
    frame_indices = [int(x * total_frames / num_frames) for x in range(num_frames)]

    # Start frame extraction
    count = 0
    success = True
    while success:
        success, frame = video.read()

        if count in frame_indices:
            frame_path = os.path.join(output_folder, f"frame_{count}.jpg")
            cv2.imwrite(frame_path, frame)

        count += 1

    # Release the video capture object
    video.release()

    # print(f"Frames from a video extracted successfully: {count-1}")

def extract_frames_from_folder(folder_path, output_folder, num_frames):
    # Iterate over all files in the folder
    print(f"Begin extracting frames from {folder_path}...")
    num_videos = 0
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".mp4"):
            video_path = os.path.join(folder_path, file_name)
            video_name = os.path.splitext(file_name)[0]
            video_output_folder = os.path.join(output_folder, video_name)
            extract_frames(video_path, video_output_folder, num_frames)
            if num_videos % 10 == 0:
                print("Number of videos done: ", num_videos)
            num_videos += 1

    print(f"All Videos extracted successfully. Total videos extracted: {num_videos} and it's stored at: {output_folder}")

# Variables Declaration
folder_path = "./datasets/train/0/"
output_folder = "./datasets/train_frames/0"
num_frames = 30

extract_frames_from_folder(folder_path, output_folder, num_frames)
