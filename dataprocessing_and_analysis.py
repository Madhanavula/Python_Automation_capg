import csv

# Define the paths for the source and destination files
source_file = r'C:\Python_Automation_Roadmap_files\Dataprocessing_and_analysis\inputdata.csv'
destination_file = r'C:\Python_Automation_Roadmap_files\Dataprocessing_and_analysis\analysis_results.csv'

# Read data from the source CSV file
data = []
with open(source_file, 'r', newline='') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)  # Read the header row
    data.append(header)
    for row in csv_reader:
        data.append(row)

# Perform calculations on the data (for example, calculate the total for a specific column)
total_column_index = 2  # Adjust this index according to your data
total = sum(float(row[total_column_index]) for row in data[1:])  # Skip the header

# Append the calculation result to the header
header.append('Total')
data[0] = header

# Append the total to each data row
for row in data[1:]:
    row.append(total)

# Save the processed data to a new CSV file
with open(destination_file, 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(data)

print(f"Data processing completed. Processed data saved to {destination_file}")
