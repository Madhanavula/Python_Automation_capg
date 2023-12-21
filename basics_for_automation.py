import os
import shutil


# Example: List all files in a directory
files = os.listdir(r'C:\Python_Automation_Roadmap_files\file_and_folder_mang')
for file in files:
    print(file)


shutil.copy(r'C:\Python_Automation_Roadmap_files\file_and_folder_mang\TextFiles\4_microbots.txt', r'C:\Python_Automation_Roadmap_files')
