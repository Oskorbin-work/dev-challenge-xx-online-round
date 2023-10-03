""" This code executes:
    a) checks to exist or not exist sheet cell
"""

# Import project Modules
import database.requests as db_excel


def check_true_false_cell(sheet_title, cell_name):
    """
    check_true_false_cell (request.method is POST ) checks exist sheet cell or not exist
    :param sheet_title: sheet title
    :param cell_name: cell name
    :return: True is exist, False isn't exist
    """
    status_title = db_excel.get_check_exist_cell(sheet_title,cell_name)[0][0]
    if status_title == 1:
        return True
    else:
        return False