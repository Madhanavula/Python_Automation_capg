import openpyxl

# Create a new workbook
workbook = openpyxl.Workbook()

# Select a sheet
sheet = workbook.active

# Write data to cells
sheet['A1'] = 'Name'
sheet['B1'] = 'Age'

data = [('John', 25), ('Alice', 30), ('Bob', 22)]

for row_index, (name, age) in enumerate(data, start=2):
    sheet[f'A{row_index}'] = name
    sheet[f'B{row_index}'] = age

# Save the workbook
workbook.save(r'C:\Python_Automation_Roadmap_files\file1.xlsx')
