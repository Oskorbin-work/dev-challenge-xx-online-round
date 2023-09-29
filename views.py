""" This code executes:
1) GET:
    a) gets information about all sheets
    b) gets information about any sheet
"""
# Import flask Modules
from flask import jsonify, abort, redirect, url_for
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
    # checks sheet is exist
    check_sheet = db_excel.get_necessary_sheet(sheet_title)
    if check_sheet == []:
        # creates a new sheet where title is arg1 -- cells_of_the_sheet
        cells_of_the_sheet = db_excel.get_all_cells_of_necessary_sheet(db_excel.insert_sheet(sheet_title))
    else:
        # Gets cells of a necessary sheet
        cells_of_the_sheet = db_excel.get_all_cells_of_necessary_sheet(sheet_title)
    if cells_of_the_sheet == []:
            return {}
            # Converts format cells of a necessary sheet to json-format
    cells_of_the_sheet = convert_response(cells_of_the_sheet)
    if not cells_of_the_sheet:
        abort(404)
    return jsonify(cells_of_the_sheet)


@app.route("/", methods=['GET', 'POST'], strict_slashes=False )
def redirect_main():
    """
    redirect_main redirects user from URL "/" or "" to URL "api/v1/"
    :return: path to URL "api/v1/"
    """
    return redirect(url_for("get_sheets"))
