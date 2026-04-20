import os
import shutil

# Step 1: User se folder path lo
folder_path = input("Enter folder path where images are stored: ").strip()

# Step 2: Data mapping (image → output names)
data = {
    "osho99.jpg": [
        "Tao Upanishad 56.jpg",
        "Tao Upanishad 57.jpg",
        "Tao Upanishad 58.jpg",
        "Tao Upanishad 59.jpg",
        "Tao Upanishad 60.jpg"
    ],
    "osho55.jpg": [
        "Bin Bati Bin Tel 06.jpg",
        "Bin Bati Bin Tel 07.jpg",
        "Bin Bati Bin Tel 08.jpg",
        "Bin Bati Bin Tel 09.jpg",
        "Bin Bati Bin Tel 10.jpg"
    ],
    "osho95.jpg": [
        "Mahaveer Vani 26.jpg",
        "Mahaveer Vani 27.jpg",
        "Mahaveer Vani 28.jpg",
        "Mahaveer Vani 29.jpg",
        "Mahaveer Vani 30.jpg"
    ]
}

# Step 3: Process images
for image_name, new_names in data.items():
    source_path = os.path.join(folder_path, image_name)

    if not os.path.exists(source_path):
        print(f"❌ Image not found: {image_name}")
        continue

    for new_name in new_names:
        destination_path = os.path.join(folder_path, new_name)
        shutil.copy(source_path, destination_path)
        print(f"✅ Created: {new_name}")

print("\n🔥 Done! All images duplicated and renamed.")