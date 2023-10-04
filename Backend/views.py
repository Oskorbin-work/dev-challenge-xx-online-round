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
import functions.GET.cell as get_cell
import functions.POST.cell as post_cell
import tests.run as test_run


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
    necessary_sheet does response to a request "get necessary sheet information"
    :param sheet_title: all data sheet
    :return: response to a request in the format of json
    """
    def get_necessary_sheet(sheet_title):
        """
        get_necessary_sheet for GET method
        :param sheet_title: necessary title
        :return: response to a request
        """
        status_sheep = get_sheet.check_exist_sheep(sheet_title)
        if status_sheep:
            # Gets cells of a necessary sheet
            cells_of_the_sheet = db_excel.get_all_cells_of_necessary_sheet(sheet_title)
            if cells_of_the_sheet == []:
                return {}
            # Converts format cells of a necessary sheet to json-format
            return common_sheet.convert_response(cells_of_the_sheet,sheet_title)
        else:
            abort(404)

    def post_necessary_sheet(old_title):
        """
        post_necessary_sheet for POST method
        :param sheet_title: necessary title
        :return: response to a request
        """
        new_title = request.json.get('title')
        status_title = post_sheet.check_exist_sheep(new_title, old_title)
        if status_title == 200:
            if new_title is None:
                new_title = old_title
            return get_necessary_sheet(new_title)
        else:
            abort(status_title)



    if request.method == "GET":
        return jsonify(get_necessary_sheet(sheet_title))
    elif request.method == "POST":
        return jsonify(post_necessary_sheet(sheet_title))
    else:
        return {"Wrong request method": request.method}


@app.route(ENDPOINT + '<sheet_title>/' + '<cell_name>', methods=['GET', 'POST'])
@app.route(ENDPOINT + '<sheet_title>/' + '<cell_name>/', methods=['GET', 'POST'])
def necessary_sheet_cell(sheet_title, cell_name):
    """
    necessary_sheet_cell does response to a request "get necessary sheet cell information"
    :param sheet_title: necessary sheet.
    :param cell_name: cell name
    :return: response to a request in the format of json
    """
    def check_sheet(sheet_title):
        """
         check_sheet check exist sheet
         :param sheet_title: sheet title
         """
        # sheet isn't exciting
        if not common_sheet.check_true_false_sheet(sheet_title):
            abort(404)

    def get_necessary_cell(sheet_title, cell_name):
        """
        get_necessary_cell for GET method
        :param sheet_title: sheet title
        :param cell_name: cell name
        :return: response to a request
        """
        status_cell = get_cell.check_exist_sheep_cell(sheet_title, cell_name)
        if status_cell:
            # get sheet cell
            cell = db_excel.get_necessary_sheet_cell(sheet_title, cell_name)[0]
            return cell
        else:
            abort(404)

    def post_necessary_cell(sheet_title, old_cell):
        """
         post_necessary_cell for POST method
         :param sheet_title: sheet title
         :param cell_name: cell name
         :return: response to a request
         """
        new_cell = request.json.get('name')
        new_value = request.json.get('value')

        status_cell = post_cell.check_exist_sheet_cell(sheet_title, new_cell, old_cell,new_value)
        if status_cell == 201:
            if new_cell is None:
                new_cell = old_cell
            return get_necessary_cell(sheet_title, new_cell)
        else:
            abort(status_cell)

    check_sheet(sheet_title)
    if request.method == "GET":
        return jsonify(get_necessary_cell(sheet_title, cell_name))
    elif request.method == "POST":
        return jsonify(post_necessary_cell(sheet_title, cell_name))
    else:
        return {"Wrong request method": request.method}


@app.route("/", methods=['GET', 'POST'], strict_slashes=False)
def redirect_main():
    """
    Redirect_main redirects user from URL "/" or "" to URL "api/v1/"
    :return: path to URL "api/v1/"
    """
    return redirect(url_for("get_sheets"))


@app.route(ENDPOINT +"/tests", methods=['GET'], strict_slashes=False)
def tests():
    """
    run tests
    """
    return test_run.run_tests()




