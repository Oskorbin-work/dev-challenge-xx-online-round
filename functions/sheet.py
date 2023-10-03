""" This code executes:
    a) checks to exist or not exist sheet
"""
# Import project Modules
import database.requests as db_excel
import functions.POST.formulas.formulas as formula


def convert_response(cells_of_the_sheet,sheet_title):
    """
     convert_response does convert format response to necessary format
    :param cells_of_the_sheet: all data sheet
    :param sheet_title: sheet title
    :return: necessary format response
    """
    result = dict()
    for cell in cells_of_the_sheet:
        new_result = get_new_result(cell["value"], cell["name"], sheet_title)
        temp = db_excel.update_old_cell_result(sheet_title, cell["name"], new_result)
        result[cell["name"]] = {"value": cell["value"], "result": new_result}
    return result


def common_check_sheet(sheet_title):
    """
     common_check_sheet it not actual def
    :param sheet_title: name title
    :return: get necessary sheet
    """
    return db_excel.get_necessary_sheet(sheet_title)


def check_true_false_sheet(sheet_title):
    """
    check_true_false_sheet (request.method is POST ) checks exist sheet or not exist
    :param sheet_title:
    :param sheet title
    :return: True is exist, False isn't exist
    """
    status_title = db_excel.get_check_exist_sheet(sheet_title)[0][0]
    if status_title == 1:
        return True
    else:
        return False


def get_new_result(value, name_cell, sheet_title):
    """
    get_new_result get result cell
    :param value: value cell
    :param name_cell: current cell
    :param sheet_title: current sheet.
    :return: new result
    """
    return formula.get_value_formula(value,name_cell, sheet_title)