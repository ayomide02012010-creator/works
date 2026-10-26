import openpyxl as xl

wb = xl.load_workbook("transactions.xlsx")

sheet = wb["Sheet1"]
for row in sheet.values:
    print(row[2]*0.9)
          


