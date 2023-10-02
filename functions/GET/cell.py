# Import project Modules
import database.requests as db_excel


def check_exist_sheep_cell(sheet_title, cell_name):
    check_cell = db_excel.get_necessary_sheet_cell(sheet_title, cell_name)
    if check_cell == []:
        return False
    else:
        return True
