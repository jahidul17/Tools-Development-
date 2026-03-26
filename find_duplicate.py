import os
import hashlib
import shutil
from PIL import Image

def get_image_hash(image_path):
    """Creates a unique hash for an image using Average Hashing"""
    try:
        with Image.open(image_path) as img:
            # Resize and convert to grayscale for speed and accuracy
            img = img.resize((16, 16), Image.Resampling.LANCZOS).convert('L')
            pixels = list(img.getdata())
            avg = sum(pixels) / len(pixels)
            bits = "".join(['1' if p > avg else '0' for p in pixels])
            return hashlib.md5(bits.encode()).hexdigest()
    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return None

def move_duplicate_images(source_folder):
    # Create a new folder to store duplicates
    output_folder = os.path.join(source_folder, "duplicates_found")
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    hashes = {}
    move_count = 0

    print("Scanning images, please wait...")

    for filename in os.listdir(source_folder):
        # Only check files in the root folder, not the newly created duplicates folder
        file_path = os.path.join(source_folder, filename)
        
        if os.path.isfile(file_path) and filename.lower().endswith(('png', 'jpg', 'jpeg', 'gif', 'bmp')):
            img_hash = get_image_hash(file_path)
            
            if img_hash:
                if img_hash in hashes:
                    # Duplicate found, move it
                    dest_path = os.path.join(output_folder, filename)
                    
                    # If a file with the same name already exists in the duplicates folder
                    if os.path.exists(dest_path):
                        dest_path = os.path.join(output_folder, "dup_" + filename)
                    
                    shutil.move(file_path, dest_path)
                    move_count += 1
                    print(f"Moved: {filename}")
                else:
                    # Store hash of the original image
                    hashes[img_hash] = file_path

    print("-" * 30)
    print(f"Task Complete! Total {move_count} duplicate images moved to: '{output_folder}'")

# Path to your dataset
folder_path = r"E:\TheZahids\Final year Thesis\Code\Passenger_Shed_Dataset\Test" 
move_duplicate_images(folder_path)