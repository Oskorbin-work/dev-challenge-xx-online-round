""" This code executes:
1) working with sql-requests;
"""
# Import project Modules
from database.decorators import request_bd_select, request_bd_insert, request_bd_select_easy, request_bd_update


@request_bd_select
def get_all_sheets():
    """
    get_all_sheet does get all sheets information
    :return: all sheets information
    """
    return f"select * from sheets"


@request_bd_select
def get_all_cells_of_necessary_sheet(sheet_title):
    """
    get_all_cells_of_sheet does get all cells of necessary sheet
    :param sheet_title: title sheet
    :return: all cells of a necessary sheet
    """
    return (f"select * from cells as A "
            f"join sheets as B "
            f"on A.sheet_id=B.id "
            f"where B.title='{sheet_title}'")


@request_bd_select
def get_update_all_cells_of_necessary_sheet(sheet_title):
    """
    get_update_all_cells_of_necessary_sheet does get all cells of necessary sheet
    :param sheet_title:  title sheet
    :return:  name, value and result cells of a necessary sheet
    """
    return (f"select A.name,A.value,A.result from cells as A "
            f"join sheets as B "
            f"on A.sheet_id=B.id "
            f"where B.title='{sheet_title}'")


@request_bd_select
def get_necessary_sheet(sheet_title):
    """
    get_necessary_sheet does get necessary sheet information
    :param sheet_title: title sheet
    :return: necessary sheet information
    """
    return f"select * from sheets where title='{sheet_title}' limit 1"


@request_bd_select
def get_necessary_sheet_cell(sheet_title, cell_name):
    """
    get_necessary_sheet_cell does get necessary sheet cell information
    :param sheet_title: title sheet
    :param cell_name: cell name
    :return: necessary sheet cell information
    """
    id_sheet_test = get_id_necessary_sheet(sheet_title)
    id_sheet = int()
    for i in id_sheet_test:
        id_sheet = int(i[0])
    return f"select name,value, result from cells where sheet_id='{id_sheet}' and name='{cell_name}'  limit 1"


@request_bd_select_easy
def get_check_exist_cell(sheet_title, cell_name):
    """
    get_check_exist_cell does check exist a cell
    :param sheet_title: name
    :param cell_name: cell name
    :return: 1 or 0.1 is True, 0 is False
    """
    id_sheet_test = get_id_necessary_sheet(sheet_title)
    id_sheet = int()
    for i in id_sheet_test:
        id_sheet = int(i[0])
    return f"select exists(select * from cells where name='{cell_name}' and sheet_id={id_sheet})"


@request_bd_select_easy
def get_check_exist_sheet(sheet_title):
    """
    get_check_exist_sheet does check exist a sheet
    :param sheet_title: name title
    :return: 1 or 0. 1 is True, 0 is False
    """
    return f"select exists(select * from sheets where title='{sheet_title}')"


@request_bd_select_easy
def get_id_necessary_sheet(sheet_title):
    """
    get_id_necessary_sheet does get id necessary a sheet
    :param sheet_title: name title
    :return: id necessary a sheet
    """
    return f"select id from sheets where title='{sheet_title}'"


@request_bd_select_easy
def get_id_necessary_cell(sheet_title, cell_name):
    """
    get_id_necessary_cell does get id necessary a cell
    :param sheet_title: name title
    :param cell_name: cell name
    :return: id necessary a cell
    """
    id_old_sheet_test = get_id_necessary_sheet(sheet_title)
    id_old_sheet = int()
    for i in id_old_sheet_test:
        id_old_sheet = int(i[0])

    return f"select id from cells where name='{cell_name}' and sheet_id={id_old_sheet}"


@request_bd_insert
def insert_sheet(sheet_title):
    """
    insert_sheet does insert new sheet
    :param sheet_title: name title
    :return: sql-insert
    """
    return f"insert into sheets (title) values ('{sheet_title}')"


@request_bd_insert
def insert_sheet_cell(sheet_title, cell_name):
    """
    insert_sheet_cell does insert new cell
    :param sheet_title: name title
    :param cell_name: cell name
    :return: sql-insert
    """
    id_old_sheet_test = get_id_necessary_sheet(sheet_title)
    id_sheet = int()
    for i in id_old_sheet_test:
        id_sheet = int(i[0])
    return f"insert into cells (sheet_id,name) values ('{id_sheet}','{cell_name}')"


@request_bd_update
def update_sheet(new_title, old_title):
    """
    update_sheet does update title sheet
    :param new_title: new title (from POST json 'title')
    :param old_title: necessary title
    :return: trash:)
    """
    id_old_sheet_test = get_id_necessary_sheet(old_title)
    id_old_sheet = int()
    for i in id_old_sheet_test:
        id_old_sheet = int(i[0])
    return f"update sheets SET title = '{new_title}' WHERE id = {id_old_sheet}"


@request_bd_update
def update_new_cell(sheet_title, new_cell, old_cell, new_result, new_value=""):
    """
    update_new_cell does update name, value and result cell.
    :param sheet_title: current sheet.
    :param new_cell: cell name
    :param old_cell: current cell
    :param new_result: new result cell
    :param new_value: new value cell
    :return: trash:)
    """
    update_change_all_old_names_cell(sheet_title, new_cell, old_cell)
    id_old_sell_test = get_id_necessary_cell(sheet_title, old_cell)
    id_old_cell = int()
    for i in id_old_sell_test:
        id_old_cell = int(i[0])

    return f"update cells SET name = '{new_cell}',value = '{new_value}',result='{new_result}' WHERE id = {id_old_cell}"


@request_bd_update
def update_old_cell(sheet_title, new_cell, old_cell, new_result, new_value=""):
    """
    update_old_cell does update value and result cell.
    :param sheet_title: current sheet.
    :param new_cell: cell name
    :param old_cell: current cell
    :param new_result: new result cell
    :param new_value: new value cell
    :return: trash:)
    """
    id_old_sell_test = get_id_necessary_cell(sheet_title, old_cell)
    id_old_cell = int()
    for i in id_old_sell_test:
        id_old_cell = int(i[0])
    return f"update cells SET value = '{new_value}',result='{new_result}' WHERE id = {id_old_cell}"


def update_change_all_old_names_cell(sheet_title, new_name, old_name):
    """
    update_change_all_old_names_cell does update value and result cell.
    :param sheet_title: current sheet.
    :param new_name: cell name
    :param old_name: current cell
    """
    list_of_data = [cell for cell in get_update_all_cells_of_necessary_sheet(sheet_title)]
    for cell in list_of_data:
        cell["value"] = cell["value"].replace(old_name, new_name)
        temp = update_old_cell(sheet_title, new_name, cell["name"], cell["result"], cell["value"])


@request_bd_update
def update_old_cell_result(sheet_title, old_cell, new_result):
    """
     update_old_cell_result does update value and result cell.
     :param sheet_title: current sheet.
     :param old_cell: current cell
     :param new_result: new result cell
     :return: trash:)
     """
    id_old_sell_test = get_id_necessary_cell(sheet_title, old_cell)
    id_old_cell = int()
    for i in id_old_sell_test:
        id_old_cell = int(i[0])
    return f"update cells SET result='{new_result}' WHERE id = {id_old_cell}"
