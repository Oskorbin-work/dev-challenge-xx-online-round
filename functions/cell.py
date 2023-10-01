# Import project Modules
import database.requests as db_excel


def check_exist_sheep_cell(sheet_title, cell_name, method):
    """
    Check_exist_sheep_cell checks sheep cell exist. If not exist then creates a new cell.
    """
    # get sheet cell
    sheet_id = db_excel.get_necessary_sheet(sheet_title)[0]['id']
    check_cell = db_excel.get_necessary_sheet_cell(sheet_id, cell_name)
    if method == "GET":
        if check_cell == []:
            return False
        else:
            return True
    elif method == "POST":
        if check_cell == []:
            temp_value = db_excel.insert_sheet_cell(sheet_id, cell_name)
            return True
        else:
            return True


