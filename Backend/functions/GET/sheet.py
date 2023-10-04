""" This code executes:
    a) checks to exist or not exist sheep
"""
# Import project Modules
import database.requests as db_excel
import functions.sheet as common_sheet


def check_exist_sheep(sheet_title):
    """
    check_exist_sheep (request.method is GET ) checks sheep exist. If not exist then creates a new sheet.
    :param sheet_title: title sheet
    :return: if exist is True. if not exist is False
    """
    # checks sheet is exist
    check_sheet = common_sheet.common_check_sheet(sheet_title)
    if check_sheet == []:
        return False
    else:
        return True
