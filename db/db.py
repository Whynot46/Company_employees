from openpyxl import load_workbook

wb_staff= load_workbook('./db/staff.xlsx')
staff = wb_staff['staff']

def save_data_base():
    wb_staff.save('./db/staff.xlsx')
