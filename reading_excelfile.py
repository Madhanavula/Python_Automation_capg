import openpyxl

# Load the workbook
workbook = openpyxl.load_workbook(r'C:\Users\AVULABAB\Downloads\Asset Inventory.xlsx')

# Select a sheet
sheet = workbook['IPAM']

# Access cell values
cell_value = sheet['C3'].value
print(f'Cell C3: {cell_value}')

# Iterate through rows
for row in sheet.iter_rows(min_row=3, max_row=10, values_only=True):
    print(row)
