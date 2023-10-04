""" This code executes:
    a) checks to exist or not exist sheet cell
    b) update result cell
    c) insert cell
"""
# Import python Modules
import re
# Import project Modules
import database.requests as db_excel
import functions.cell as common_sheet
import functions.POST.formulas.formulas as formula


def check_exist_sheet_cell(sheet_title, new_cell, old_cell, new_value):
    """
    check_exist_sheet_cell (request.method is POST) checks whether there is an old cell, new value or not. Then, using if, it decides what will happen next.
    :param sheet_title: it current sheet.
    :param new_cell: new name cell
    :param old_cell: current cell
    :param new_value: new value cell
    :return: status code. 422 -- if has wrong cell (old or new) or value, 201 is ok.
    """
    status_name = 201
    # JSON POST -- {"name": "var2", "value": "something"}
    if new_cell and (new_value or new_value is ""):
        status_name = new_cell_new_value(sheet_title, new_cell, old_cell, new_value)
    # JSON POST -- {}... Not has "name" and "value"
    elif new_cell is None and new_value is None:
        status_name = new_cell_without_parameters(sheet_title, old_cell)
    # JSON POST -- {"name": "var2"}... Not has "value"
    elif new_cell and new_value is None:
        status_name = new_cell_without_new_value(sheet_title, new_cell, old_cell)
    # JSON POST -- {"value": "something"}... Not has "name"
    elif new_cell is None and (new_value or new_value is ""):
        old_cell_new_value(sheet_title, old_cell, new_value)
    else:
        status_name = 422

    return status_name


def new_cell_new_value(sheet_title, new_cell, old_cell, new_value):
    """
    new_cell_new_value (request.method is POST) update new name cell and value
    :param sheet_title: it current sheet
    :param new_cell: new name cell
    :param old_cell: current cell
    :param new_value: new value cell
    :return: status code. 422 -- if has wrong cell (old or new) or value, 201 is ok.
    """
    # text error check cells
    exist_new_cell = common_sheet.check_true_false_cell(sheet_title, new_cell)
    exist_old_cell = common_sheet.check_true_false_cell(sheet_title, old_cell)
    if exist_old_cell is False and old_cell is not None:
        return 422
    if exist_old_cell:
        # update
        if exist_new_cell is False:
            status_name = update_old_sheet_cell(sheet_title,new_cell, old_cell, new_value)
            return status_name
    return 201


def new_cell_without_parameters(sheet_title, new_cell):
    """
    new_cell_without_parameters (request.method is POST) insert new cell
    :param sheet_title: it current sheet.
    :param new_cell: new name cell
    :return: status code. 409 -- the new cell name has already been created until request, 201 is ok.
    """
    # text error check cells
    exist_new_cell = common_sheet.check_true_false_cell(sheet_title, new_cell)
    if exist_new_cell:
        return 409
    elif exist_new_cell is False:
        temp_value = db_excel.insert_sheet_cell(sheet_title, new_cell)

    return 201


def new_cell_without_new_value(sheet_title, new_cell, old_cell):
    """
    new_cell_without_new_value (request.method is POST) update name cell
    :param sheet_title: it current sheet.
    :param new_cell: new name cell
    :return: status code. 409 -- the new cell name has already been created until request, 201 is ok.
    """
    # text error check cells
    exist_new_cell = common_sheet.check_true_false_cell(sheet_title, new_cell)
    exist_old_cell = common_sheet.check_true_false_cell(sheet_title, old_cell)
    if exist_old_cell is False and old_cell is not None:
        return 422
    if exist_old_cell:
        # update
        if exist_new_cell is False:
            status_name = update_old_sheet_cell(sheet_title,new_cell, old_cell)
            return status_name
    return 201


def old_cell_new_value(sheet_title, old_cell, new_value):
    """
    old_cell_new_value (request.method is POST) update old name cell and value
    :param sheet_title: it current sheet.
    :param old_cell: current cell
    :param new_value: new value cell
    :return: status code. 422 -- if has wrong cell (old or new) or value, 201 is ok.
    """
    # text error check cells
    exist_old_cell = common_sheet.check_true_false_cell(sheet_title, old_cell)
    if exist_old_cell is False and old_cell is not None:
        return 422
    if exist_old_cell:
        # update
        new_result = get_new_result(new_value, old_cell, sheet_title)

        status_name = db_excel.update_old_cell(sheet_title, "None", old_cell, new_result,new_value)
        return status_name
    return 201


def update_old_sheet_cell(sheet_title, new_cell, old_cell, new_value=""):
    """
    update_old_sheet_cell (request.method is POST) update old name cell.
    :param sheet_title: it current sheet.
    :param old_cell: current cell
    :param new_value: new value cell
    :return: status code. 422 -- if has wrong cell (old or new), 201 is ok.
    """
    status_name = check_name_cell(new_cell)
    if status_name == 201:
        new_result = get_new_result(new_value,new_cell, sheet_title)

        temp_value = db_excel.update_new_cell(sheet_title, new_cell, old_cell, new_result, new_value)
    return status_name


def check_name_cell(cell):
    """
    check_name_cell (request.method is POST )text error check name cell (read https://support.microsoft.com/en-gb/office/use-a-screen-reader-to-name-a-cell-or-data-range-in-excel-e8b55e7a-2cfd-40c4-9ea9-e738aa24e32c).
    :param cell: name cell
    :return: status title. 422 -- if has wrong name cell, 201 is ok.
    """
    unable_rules = ["", None]
    if cell in unable_rules:
        return 422
    elif bool(re.search("^[^a-zA-Z_]|\s",cell))==True:
        return 422
    else:
        return 201


def get_new_result(value, name_cell, sheet_title):
    """
    get_new_result get result cell
    :param value: value cell
    :param name_cell: current cell
    :param sheet_title: current sheet.
    :return: new result
    """
    return formula.get_value_formula(value,name_cell, sheet_title)