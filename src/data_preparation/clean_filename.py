import os

def rename_images(base_path):
  # Iterate through each folder in the base directory
  for folder in os.listdir(base_path):
    folder_path = os.path.join(base_path, folder)
    if os.path.isdir(folder_path):
      # List all files in the folder and sort them to maintain order
      files = sorted(os.listdir(folder_path))
      for idx, file_name in enumerate(files, start=1):
        # Construct the new file name
        new_file_name = f"{folder}_{idx}{os.path.splitext(file_name)[1]}"
        # Rename the file
        os.rename(os.path.join(folder_path, file_name), os.path.join(folder_path, new_file_name))

# Path to the base directory containing ingredient folders
base_path = "/Users/bestc/Code Projects/COMO AI/data/processed/Ingredients Images"
rename_images(base_path)
