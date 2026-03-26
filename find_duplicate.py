import os
import hashlib
import shutil
from PIL import Image

def get_image_hash(image_path):
    """ছবির একটি ইউনিক হ্যাশ তৈরি করে"""
    try:
        with Image.open(image_path) as img:
            # ছবির সাইজ ছোট করে হ্যাশ তৈরি (স্পিড এবং একুরেসির জন্য)
            img = img.resize((16, 16), Image.Resampling.LANCZOS).convert('L')
            pixels = list(img.getdata())
            avg = sum(pixels) / len(pixels)
            bits = "".join(['1' if p > avg else '0' for p in pixels])
            return hashlib.md5(bits.encode()).hexdigest()
    except:
        return None

def move_duplicate_images(source_folder):
    # ডুপ্লিকেট রাখার জন্য নতুন ফোল্ডার তৈরি
    output_folder = os.path.join(source_folder, "duplicates_found")
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    hashes = {}
    move_count = 0

    print("ছবি স্ক্যান করা হচ্ছে, দয়া করে অপেক্ষা করুন...")

    for filename in os.listdir(source_folder):
        # মূল ফোল্ডারের ফাইলগুলো শুধু চেক করবে, নতুন তৈরি করা ডুপ্লিকেট ফোল্ডার নয়
        file_path = os.path.join(source_folder, filename)
        
        if os.path.isfile(file_path) and filename.lower().endswith(('png', 'jpg', 'jpeg', 'gif', 'bmp')):
            img_hash = get_image_hash(file_path)
            
            if img_hash:
                if img_hash in hashes:
                    # ডুপ্লিকেট পাওয়া গেছে, মুভ করো
                    dest_path = os.path.join(output_folder, filename)
                    
                    # যদি একই নামের ফাইল ডুপ্লিকেট ফোল্ডারে আগে থেকেই থাকে
                    if os.path.exists(dest_path):
                        dest_path = os.path.join(output_folder, "dup_" + filename)
                    
                    shutil.move(file_path, dest_path)
                    move_count += 1
                    print(f"Moved: {filename}")
                else:
                    hashes[img_hash] = file_path

    print("-" * 30)
    print(f"কাজ শেষ! মোট {move_count} টি ডুপ্লিকেট ছবি '{output_folder}' ফোল্ডারে সরানো হয়েছে।")

# আপনার ফোল্ডারের পাথ এখানে দিন (যেমন: "C:/MyPhotos")
folder_path = r"E:\TheZahids\Final year Thesis\Code\Passenger_Shed_Dataset\Test" 
move_duplicate_images(folder_path)

