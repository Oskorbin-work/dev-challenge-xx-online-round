# Import project Modules
import database.requests as db_excel


def convert_response(cells_of_the_sheet):
    """
     convert_response does convert format response to necessary format
    :param cells_of_the_sheet: all data sheet
    :return: necessary format response
    """
    result = dict()
    for cell in cells_of_the_sheet:
        result[cell["name"]] = {"value": cell["value"], "result": cell["result"]}
    return result


def cheek_sheet(sheet_title):
    """
     cheek_sheet it not actual def
    :param sheet_title: name title
    :return: get necessary sheet
    """
    return db_excel.get_necessary_sheet(sheet_title)


def check_true_false_sheet(sheet_title):
    status_title = db_excel.get_check_exist_sheet(sheet_title)[0][0]
    if status_title == 1:
        return True
    else:
        return False