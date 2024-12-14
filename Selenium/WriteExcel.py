import openpyxl
# file/workbook/sheet/loop/save
file = "C:\\Users\\RAHUL\\OneDrive\\ドキュメント\\Data.xlsx"
workbook = openpyxl.load_workbook(file)
sheet = workbook.active

for r in range(1, 5):
    for c in range(1, 3):
        sheet.cell(r, c).value = 'Welcome'
        workbook.save(file)
