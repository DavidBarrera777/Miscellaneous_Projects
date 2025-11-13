import os
import random
import subprocess
import platform

# Path to the folder with your photos
folder_path = "photos"  # change this to your folder

# Get all files in the folder
files = os.listdir(folder_path)

# Filter only images
image_files = [f for f in files if f.lower().endswith((".jpg", ".jpeg", ".png", ".gif"))]

if not image_files:
    print("No images found in the folder.")
else:
    # Pick a random image
    random_image = random.choice(image_files)
    image_path = os.path.join(folder_path, random_image)

    print("Opening:", image_path)

    # Detect OS and open image in default viewer
    if platform.system() == "Windows":
        os.startfile(image_path)  # opens in Photos by default
    elif platform.system() == "Darwin":  # macOS
        subprocess.run(["open", image_path])
    else:  # Linux
        subprocess.run(["xdg-open", image_path])
