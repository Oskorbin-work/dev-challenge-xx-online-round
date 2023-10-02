""" This code executes:
1) working with sql-request;
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
    :return: all cell of necessary sheet
    """
    return (f"select * from cells as A "
            f"join sheets as B "
            f"on A.sheet_id=B.id "
            f"where B.title='{sheet_title}'")


@request_bd_select
def get_necessary_sheet(sheet_title):
    """
    get_necessary_sheet does get necessary sheet information
    :return: necessary sheet information
    """
    return f"select * from sheets where title='{sheet_title}' limit 1"


@request_bd_select
def get_necessary_sheet_cell(sheet_title, cell_name):
    """
    get_necessary_sheet_cell does get necessary sheet cell information
    :return: necessary sheet cell information
    """
    id_sheet_test = get_id_necessary_sheet(sheet_title)
    id_sheet = int()
    for i in id_sheet_test:
        id_sheet=int(i[0])
    return f"select value,result from cells where sheet_id='{id_sheet}' and name='{cell_name}'  limit 1"

@request_bd_select_easy
def get_check_exist_cell(sheet_title, cell_name):
    """
    get_check_exist_cell does check exist a cell
    :param sheet_title: name title.cell_name: cell name
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
def get_id_necessary_cell(sheet_title,cell_name):
    """
    get_id_necessary_cell does get id necessary a cell
    :param sheet_title: name title, cell_name: cell name
    :return: id necessary a cell
    """
    id_old_sheet_test = get_id_necessary_sheet(sheet_title)
    id_old_sheet = int()
    for i in id_old_sheet_test:
        id_old_sheet=int(i[0])

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
    insert_sheet does insert new sheet
    :param sheet_title: name title
    :return: sql-insert
    """
    id_old_sheet_test = get_id_necessary_sheet(sheet_title)
    id_sheet = int()
    for i in id_old_sheet_test:
        id_sheet=int(i[0])
    return f"insert into cells (sheet_id,name) values ('{id_sheet}','{cell_name}')"


@request_bd_update
def update_sheet(new_title, old_title):
    """
    get_id_necessary_sheet does update title sheet
    :param new_title: new title (from POST json 'title'), old_title: necessary title
    :return: trash:)
    """
    id_old_sheet_test = get_id_necessary_sheet(old_title)
    id_old_sheet = int()
    for i in id_old_sheet_test:
        id_old_sheet=int(i[0])
    return f"update sheets SET title = '{new_title}' WHERE id = {id_old_sheet}"


@request_bd_update
def update_new_cell(sheet_title, new_cell, old_cell, new_value=""):
    """
    update_new_cell does update name and value cell.
   :param sheet_title: it current sheet. new_cell: new name cell, old_cell: current cell, new_value: new value cell
    :return: trash:)
    """
    id_old_sell_test = get_id_necessary_cell(sheet_title, old_cell)
    id_old_cell = int()
    for i in id_old_sell_test:
        id_old_cell = int(i[0])

    return f"update cells SET name = '{new_cell}',value = '{new_value}' WHERE id = {id_old_cell}"


@request_bd_update
def update_old_cell(sheet_title, new_cell, old_cell, new_value=""):
    """
    update_old_cell does update name cell.
   :param sheet_title: it current sheet. new_cell: new name cell, old_cell: current cell, new_value: new value cell
    :return: trash:)
    """
    id_old_sell_test = get_id_necessary_cell(sheet_title, old_cell)
    id_old_cell = int()
    for i in id_old_sell_test:
        id_old_cell = int(i[0])
    return f"update cells SET value = '{new_value}' WHERE id = {id_old_cell}"

