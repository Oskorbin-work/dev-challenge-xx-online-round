""" This code executes:
1) working with sql-request;
"""
# Import project Modules
import database.connect as db_sheet


def request_bd_select(func):
    """
    Decorator process select-query the database
    :return: query result is list of sets (include names and values sql-request)
    """
    def wrapper(*args, **kwargs):
        cur = db_sheet.open_connection().cursor()
        cur.execute(func(*args, **kwargs))
        # get list of sets (include names and values sql-request)
        value = [dict((cur.description[i][0], value)
                      for i, value in enumerate(row)) for row in cur.fetchall()]
        db_sheet.close_connection(None)
        return value
    return wrapper


# Decorator for insert query the database
def request_bd_insert(func):
    """
    Decorator process insert-query the database
     :return: insert new rows.
     """
    def wrapper(*args, **kwargs):
        conn = db_sheet.open_connection()
        cur = conn.cursor()
        cur.execute(func(*args, **kwargs))
        conn.commit()
        db_sheet.close_connection(None)
        return 0  # The comparison
    return wrapper


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


@request_bd_insert
def insert_sheet(sheet_title):
    """
    insert_sheet does insert new sheet
    :return: sql-insert
    """
    return f"insert into sheets (title) values ('{sheet_title}')"

