import os

def rename_files(folder_path, prefix):
    for count, filename in enumerate(os.listdir(folder_path)):
        src = os.path.join(folder_path, filename)
        dst = os.path.join(folder_path, f"{prefix}_{count+1}.txt")
        os.rename(src, dst)
    print("Files renamed successfully.")

# Example usage
# rename_files("C:/Users/YourName/Desktop/test_folder", "file")