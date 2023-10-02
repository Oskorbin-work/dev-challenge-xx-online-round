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
import functions.GET.sheet as get_sheet
import functions.POST.sheet as post_sheet
import functions.sheet as common_sheet
from functions.cell import check_exist_sheep_cell


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
def necessary_sheet(sheet_title):
    """
    get_sheet does response to a request "get necessary sheet information"
    :param sheet_title: all data sheet
    :return: response to a request in the format of json
    """
    def get_necessary_sheet(sheet_title):
        """
        get_necessary_sheet for GET method
        :param sheet_title: necessary title
        :return: response to a request
        """
        print(sheet_title)
        status_sheep = get_sheet.check_exist_sheep(sheet_title)
        if status_sheep:
            # Gets cells of a necessary sheet
            cells_of_the_sheet = db_excel.get_all_cells_of_necessary_sheet(sheet_title)
            if cells_of_the_sheet == []:
                return {}
            # Converts format cells of a necessary sheet to json-format
            return common_sheet.convert_response(cells_of_the_sheet)
        if not status_sheep:
            abort(404)

    def post_necessary_sheet(sheet_title):
        """
        post_necessary_sheet for POST method
        :param sheet_title: necessary title
        :return: response to a request
        """
        new_title = request.json.get('title')
        status_title = post_sheet.check_exist_sheep(new_title, sheet_title)
        if status_title == 200:
            if new_title is None:
                new_title = sheet_title
            return get_necessary_sheet(new_title)
        else:
            abort(status_title)



    if request.method == "GET":
        return jsonify(get_necessary_sheet(sheet_title))
    elif request.method == "POST":
        return jsonify(post_necessary_sheet(sheet_title))
    else:
        return {}


@app.route(ENDPOINT + '<sheet_title>/' + '<cell_name>', methods=['GET', 'POST'])
@app.route(ENDPOINT + '<sheet_title>/' + '<cell_name>/', methods=['GET', 'POST'])
def necessary_sheet_cell(sheet_title, cell_name):
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
    if not check_exist_sheep_cell(sheet_title, cell_name, request.method):
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




