import os

# Provide the path to the folder containing your images
folder_path = r'E:\TheZahids\Final year Thesis\Code\Passenger_Shed_Dataset\waiting area bus stand'

# List all files in the directory
files = os.listdir(folder_path)

# Loop through and rename each file one by one
for index, filename in enumerate(files):
    # Separate the file extension (e.g., .jpg or .png)
    extension = os.path.splitext(filename)[1]
    
    # Create the new name (e.g., passenger_shed5_1.jpg, passenger_shed5_2.jpg...)
    # Note: I corrected "sheed" to "shed" to match standard spelling
    new_name = f"passenger_shed5_{index + 1}{extension}"
    
    # Define source and destination paths
    source = os.path.join(folder_path, filename)
    destination = os.path.join(folder_path, new_name)
    
    # Rename the file
    try:
        os.rename(source, destination)
    except FileExistsError:
        print(f"Skipped: {new_name} already exists.")

print("All files have been successfully renamed!")

