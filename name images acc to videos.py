
import os
import random

# --- INPUT PATHS ---
video_folder = input("Enter video folder path: ").strip()
image_folder = input("Enter image folder path: ").strip()

# --- GET VIDEO NAMES (without extension) ---
video_names = []
for file in os.listdir(video_folder):
    if file.lower().endswith((".mp3")):
        name = os.path.splitext(file)[0]
        video_names.append(name)

# --- GET IMAGE FILES ---
image_files = [f for f in os.listdir(image_folder)
               if f.lower().endswith((".jpg", ".jpeg", ".png", ".webp"))]

# --- CHECK ---
if len(image_files) < len(video_names):
    print("Not enough images for videos!")
    exit()

# --- RANDOMIZE ---
random.shuffle(image_files)

# --- RENAME IMAGES BASED ON VIDEO NAMES ---
for i, video_name in enumerate(video_names):
    old_image = image_files[i]
    ext = os.path.splitext(old_image)[1]

    new_name = video_name + ext

    old_path = os.path.join(image_folder, old_image)
    new_path = os.path.join(image_folder, new_name)

    os.rename(old_path, new_path)

print("Done! Images renamed based on video names.")
