import os
import re
import datetime

log_dir = 'logs'
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

def log_activity(message, log_file):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {message}"

    log_path = os.path.join(log_dir, log_file)

    with open(log_path, 'a') as f:
        f.write(log_entry + '\n')

def extract_info_from_logs(log_file):
    pattern = r'Error: (.+)'
    with open(log_file, 'r') as file:
        log_content = file.read()
        errors = re.findall(pattern, log_content)
        return errors

log_activity("sample_message", 'log_file1.log')

# Usage
log_errors = extract_info_from_logs('C:\Python_Automation_Roadmap\logs\log_file1.log')
print("Errors found:", log_errors)
