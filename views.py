""" This code executes:
1) GET:
    a) gets information about all sheets
    b) gets information about any sheet
"""
# Import flask Modules
from flask import jsonify, abort, redirect, url_for, request
# Import project Modules
import database.requests as db_excel
from application import app
from application import client  # It is used to unit-tests
from settings import ENDPOINT


@app.route(ENDPOINT, methods=['GET'])
def get_sheets():
    """
    get_sheets does response to a request "get all sheets information"
    :return: response to a request in the format of json
    """
    data = db_excel.get_all_sheets()
    return jsonify({'Sheets': data})


@app.route(ENDPOINT + '<sheet_title>', methods=['GET', 'POST'])
@app.route(ENDPOINT + '<sheet_title>/', methods=['GET', 'POST'])
def get_necessary_sheet(sheet_title):
    """
    get_sheet does response to a request "get necessary sheet information"
    :param sheet_title: all data sheet
    :return: response to a request in the format of json
    """

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
    if check_exist_sheep(sheet_title, request.method):
        pass
        # Gets cells of a necessary sheet
        cells_of_the_sheet = db_excel.get_all_cells_of_necessary_sheet(sheet_title)
        if cells_of_the_sheet == []:
            return {}
        # Converts format cells of a necessary sheet to json-format
        cells_of_the_sheet = convert_response(cells_of_the_sheet)
    if not check_exist_sheep(sheet_title, request.method):
        abort(404)
    return jsonify(cells_of_the_sheet)


@app.route(ENDPOINT + '<sheet_title>/' + '<cell_name>', methods=['GET', 'POST'])
@app.route(ENDPOINT + '<sheet_title>/' + '<cell_name>/', methods=['GET', 'POST'])
def get_necessary_sheet_cell(sheet_title, cell_name):
    """
    get_sheet does response to a request "get necessary sheet information"
    :param sheet_title: necessary sheet.
    :param cell_name: necessary cell
    :return: response to a request in the format of json
    """
    check_exist_sheep(sheet_title, request.method)
    # if GET and sheet isn't exciting
    if not check_exist_sheep(sheet_title, request.method):
        abort(404)
    if check_exist_sheep_cell(sheet_title, cell_name, request.method):
        # get sheet cell
        sheet_id = db_excel.get_necessary_sheet(sheet_title)[0]['id']
        cell = db_excel.get_necessary_sheet_cell(sheet_id, cell_name)[0]
    # if GET and cell of a sheet isn't exciting
    if not check_exist_sheep_cell(sheet_title,cell_name, request.method):
        abort(404)
    if request.method == "GET":
        return jsonify(cell)
    elif request.method == "POST":
        return {}
    else:
        return {"Wrong request method": request.method}


@app.route("/", methods=['GET', 'POST'], strict_slashes=False)
def redirect_main():
    """
    Redirect_main redirects user from URL "/" or "" to URL "api/v1/"
    :return: path to URL "api/v1/"
    """
    return redirect(url_for("get_sheets"))


# ------------------------------------------------------------------
# additional functions
def check_exist_sheep(sheet_title, method="GET"):
    """
    Check_empty_sheep checks sheep exist. If not exist then creates a new sheet.
    """
    # checks sheet is exist
    check_sheet = db_excel.get_necessary_sheet(sheet_title)
    if method == "GET":
        if check_sheet == []:
            return False
        else:
            return True
    elif method == "POST":
        if check_sheet == []:
            temp_value = db_excel.insert_sheet(sheet_title)
            return True
        else:
            return True


def check_exist_sheep_cell(sheet_title, cell_name,method):
    """
    Check_exist_sheep_cell checks sheep cell exist. If not exist then creates a new cell.
    """
    # get sheet cell
    sheet_id = db_excel.get_necessary_sheet(sheet_title)[0]['id']
    check_cell = db_excel.get_necessary_sheet_cell(sheet_id, cell_name)
    if method == "GET":
        if check_cell == []:
            return False
        else:
            return True
    elif method=="POST":
        if check_cell == []:
            temp_value = db_excel.insert_sheet_cell(sheet_id, cell_name)
            return True
        else:
            return True
