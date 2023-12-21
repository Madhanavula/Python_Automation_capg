import os
import shutil
#ctrl+shist+p
# Define the source directory where the files are located.
source_directory = r'C:\Python_Automation_Roadmap_files\file_and_folder_mang'

# Create a dictionary to map file types to their respective directories.
file_type_mapping = {
    '.txt': 'TextFiles',
    '.png': 'ImageFiles',
    '.pdf': 'PDFFiles',
    '.pptx': 'powerpoint_files',
    '.docx':'word_files'
    # Add more file types and corresponding directory names as needed.
}

# Create subdirectories for each file type if they don't exist.
for directory_name in file_type_mapping.values():
    directory_path = os.path.join(source_directory, directory_name)
    os.makedirs(directory_path, exist_ok=True)

# Iterate over the files in the source directory.
for filename in os.listdir(source_directory):
    file_path = os.path.join(source_directory, filename)

    if os.path.isfile(file_path):
        # Get the file extension (file type).
        file_extension = os.path.splitext(filename)[1]

        # Determine the destination directory based on the file type.
        destination_directory = file_type_mapping.get(file_extension, 'OtherFiles')

        # Construct the full destination path.
        destination_path = os.path.join(source_directory, destination_directory, filename)

        # Move the file to the appropriate subdirectory.
        shutil.move(file_path, destination_path)
        print(f"Moved {filename} to {destination_directory}")

print("File organization completed.")
