""" This code executes:
1) query processing
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


def request_bd_select_easy(func):
    """
    Decorator process select-query the database
    :return: query result
    """

    def wrapper(*args, **kwargs):
        cur = db_sheet.open_connection().cursor()
        cur.execute(func(*args, **kwargs))
        # get list of sets (include names and values sql-request)
        value = cur.fetchall()
        db_sheet.close_connection(None)

        return value

    return wrapper


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


def request_bd_update(func):
    """
    Decorator process update-query the database
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
