""" This code executes:
    a) checks to exist or not exist sheet
    b) update sheet
    c) insert sheet
"""
# Import python Modules
import re
# Import project Modules
import database.requests as db_excel
import functions.sheet as common_sheet


def check_exist_sheep(new_title, old_title):
    """
    check_exist_sheep (request.method is POST ) checks sheep exist. If not exist, then create a new sheet or update
    (If have POSt json title).
    :param new_title: new title (from POST json 'title')
    :param old_title: necessary title
    :return: status title. 422 -- if has wrong title, 200 is ok. 404 -- if has wrong olt title and has new_title.
    """
    status_title = 200
    # text error check titles
    exist_new_title = common_sheet.check_true_false_sheet(new_title)
    exist_old_title = common_sheet.check_true_false_sheet(old_title)
    # has wrong olt title and has new_title.
    if exist_old_title is False and new_title is not None:
        return 404
    if exist_old_title:
        # update
        if exist_new_title is False:
            status_title = update_old_title_sheet(new_title, old_title)
        return status_title
    else:
        # insert
        temp_value = insert_new_title_sheet(old_title)
        return status_title


def insert_new_title_sheet(new_title):
    """
    insert_new_title_sheet (request.method is POST ) insert new title
    :param new_title: new title (from POST json 'title')
    :return: status title. 422 -- if has wrong title, 200 is ok. 404 -- if has wrong olt title and has new_title.
    """
    status_title = check_name_title(new_title)
    if status_title == 200:
        temp_value = db_excel.insert_sheet(new_title)
    return status_title


def update_old_title_sheet(new_title, old_title):
    """
    update_new_title_sheet (request.method is POST ) update old title
    :param new_title: new title (from POST json 'title')
    :param old_title: necessary title
    :return: status title. 422 -- if has wrong title, 200 is ok. 404 -- if has wrong olt title and has new_title.
    """
    status_title = check_name_title(new_title)
    if status_title == 200:
        temp_value = db_excel.update_sheet(new_title, old_title)
    return status_title


def check_name_title(title):
    """
    check_name_title (request.method is POST )text error check titles (read https://support.microsoft.com/ru-ru/office/%D0%BF%D0%B5%D1%80%D0%B5%D0%B8%D0%BC%D0%B5%D0%BD%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BB%D0%B8%D1%81%D1%82%D0%B0-3f1f7148-ee83-404d-8ef0-9ff99fbad1f9#:~:text=%D0%92%D0%B0%D0%B6%D0%BD%D0%BE%3A%20%D0%98%D0%BC%D0%B5%D0%BD%D0%B0%20%D0%BB%D0%B8%D1%81%D1%82%D0%BE%D0%B2%20%D0%BD%D0%B5%20%D0%BC%D0%BE%D0%B3%D1%83%D1%82,%D0%A1%D0%BE%D0%B4%D0%B5%D1%80%D0%B6%D0%B0%D1%82%D1%8C%20%D0%B1%D0%BE%D0%BB%D0%B5%D0%B5%2031%20%D0%B7%D0%BD%D0%B0%D0%BA%D0%B0.&text=%D0%9D%D0%B0%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%80%2C%2002%2F17%2F2016,%2D17%2D2016%20%E2%80%94%20%D0%BC%D0%BE%D0%B6%D0%BD%D0%BE).
    :param title:  title sheet
    :return: status title. 422 -- if has wrong title, 200 is ok. 404 -- if has wrong olt title and has new_title.
    """
    unable_rules = ["", None, "History"]
    if title in unable_rules:
        return 422
    elif len(title) >= 32:
        return 422
    elif bool(re.search("/|\?|\*|:|\[|\]",title))==True:
        return 422
    else:
        return 200


