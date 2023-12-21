import psutil
import time

# Function to monitor CPU and memory usage
def monitor_resources():
    cpu_percent = psutil.cpu_percent(interval=1)
    memory_percent = psutil.virtual_memory().percent

    print(f"CPU Usage: {cpu_percent}%")
    print(f"Memory Usage: {memory_percent}%\n")

# Function to monitor a log file
def monitor_log_file(log_file_path):
    try:
        with open(log_file_path, 'r') as log_file:
            log_content = log_file.read()
            print(f"Log File Content:\n{log_content}\n")
    except FileNotFoundError:
        print(f"Log file not found at: {log_file_path}\n")


# Main monitoring loop
while True:
    print("Monitoring System Resources:")
    monitor_resources()

    log_file_path = r"C:\Python_Automation_Roadmap\logs\logfile1.txt"
    print(f"Monitoring Log File: {log_file_path}")
    monitor_log_file(log_file_path)

    # Set a delay before the next monitoring iteration
    time.sleep(2)  # Adjust the delay as needed
