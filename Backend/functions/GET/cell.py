""" This code executes:
    a) checks to exist or not exist sheet cell
    b) update cell
"""
# Import project Modules
import database.requests as db_excel
import functions.POST.formulas.formulas as formula


def check_exist_sheep_cell(sheet_title, cell_name):
    """
    check_exist_sheep_cell checks to exist or not exist sheep cell and update result cell
    :param sheet_title: current sheet.
    :param cell_name: current cell
    :return: True -- exist, False -- not exist
    """
    check_cell = db_excel.get_necessary_sheet_cell(sheet_title, cell_name)
    new_result = get_new_result(check_cell[0]["value"], check_cell[0]["name"], sheet_title)
    temp = db_excel.update_old_cell_result(sheet_title, check_cell[0]["name"], new_result)
    if check_cell == []:
        return False
    else:
        return True


def get_new_result(value, name_cell, sheet_title):
    """
    get_new_result get result cell
    :param value: value cell
    :param name_cell: current cell
    :param sheet_title: current sheet.
    :return: new result
    """
    return formula.get_value_formula(value,name_cell, sheet_title)