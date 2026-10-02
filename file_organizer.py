import os
import shutil

# Folder containing the files to organize
source_folder = input("Enter the folder path to organize: ")

# Check if the folder exists
if not os.path.exists(source_folder):
    print("Folder not found.")
    exit()

# File categories and their extensions
file_categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z"],
    "Python": [".py"]
}

# Organize files
for filename in os.listdir(source_folder):

    file_path = os.path.join(source_folder, filename)

    # Skip folders
    if os.path.isdir(file_path):
        continue

    file_extension = os.path.splitext(filename)[1].lower()

    category_found = False

    for category, extensions in file_categories.items():

        if file_extension in extensions:

            category_folder = os.path.join(source_folder, category)

            # Create category folder if it doesn't exist
            os.makedirs(category_folder, exist_ok=True)

            destination = os.path.join(category_folder, filename)

            shutil.move(file_path, destination)

            print(f"Moved: {filename} → {category}/")

            category_found = True
            break

    # Files with extensions not listed above
    if not category_found:
        other_folder = os.path.join(source_folder, "Others")

        os.makedirs(other_folder, exist_ok=True)

        destination = os.path.join(other_folder, filename)

        shutil.move(file_path, destination)

        print(f"Moved: {filename} → Others/")

print("\nFile organization completed successfully!")