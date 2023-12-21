import os

def find_replace_in_files(directory, old_text, new_text):
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r') as file:
                content = file.read()
                new_content = content.replace(old_text, new_text)
            with open(file_path, 'w') as file:
                file.write(new_content)

# Usage
find_replace_in_files('C:\Python_Automation_Roadmap_files\Text_files', 'game', 'emotion')
