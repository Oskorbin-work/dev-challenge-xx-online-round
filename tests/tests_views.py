# Import project Modules
from views import client
from settings import ENDPOINT


# ------------------------------------------------
# test def get_sheets
def test_get_sheets():
    """
    test_get_sheets checks status code 200 while url ENDPOINT(detail in file settings.py)
    """
    print("\n" + test_get_sheets.__name__)
    res = client.get(ENDPOINT)
    # Checks that def work is ok
    assert res.status_code == 200, "sheets are missing"
    print("–   " + ENDPOINT + " has status code - 200")


def test_get_sheets_check_key_sheets():
    """
    test_get_sheets_check_key_sheets checks key Sheets in Sheets exist
    """
    print("\n" + test_get_sheets_check_key_sheets.__name__)
    res = client.get(ENDPOINT)
    assert res.get_json().get('Sheets') is not None, "Key \"Sheets\" isn't exist"
    print("–    Key \"Sheets\" is exist")


def test_get_sheets_check_key_value_sheets():
    """
    test_get_sheets_check_key_value_sheets checks key Sheets in sheets is list
    """
    print("\n" + test_get_sheets_check_key_value_sheets.__name__)
    res = client.get(ENDPOINT)
    assert isinstance(res.get_json()['Sheets'], list) is True, "Key \"Sheets\" value isn't list"
    print("–    Key \"Sheets\" value is list")


def test_get_sheets_check_key_value_sheets_contain_dict():
    """
    test_get_sheets_check_key_value_sheets_contain_dict
     checks every sheet is dict
    """
    print("\n" + test_get_sheets_check_key_value_sheets_contain_dict.__name__)
    res = client.get(ENDPOINT)
    assert all(isinstance(sheet, dict) for sheet in res.get_json()['Sheets']) is True, " \"Sheets\" Values aren't dict"
    print("–     \"Sheets\" Values aren't dict")


def test_get_sheets_count_columns():
    """
    test_get_sheets_count_columns checks dict every sheet has two columns
    """
    print("\n" + test_get_sheets_count_columns.__name__)
    res = client.get(ENDPOINT)
    test_data = set(len(sheet) for sheet in res.get_json()["Sheets"])
    assert test_data == {2}, str(test_data) + " Count sheets column isn't 2 "
    print("–    Count sheets column is 2")


def test_get_sheets_has_id():
    """
    test_get_sheets_has_id checks every id sheet is exits
    """
    print("\n" + test_get_sheets_has_id.__name__)
    res = client.get(ENDPOINT)
    assert all(sheet.get('id') is not None for sheet in res.get_json()["Sheets"]) is True, \
        "Several tables don't have attribute 'id'"
    print("–    All tables have attribute 'id'")


def test_get_sheets_has_title():
    """
    test_get_sheets_has_title checks every title sheet is exist
    """
    print("\n" + test_get_sheets_has_title.__name__)
    res = client.get(ENDPOINT)
    assert all(sheet.get('title') is not None for sheet in res.get_json()["Sheets"]) is True, \
        "Several tables don't have attribute 'title'"
    print("–    All title have attribute 'title'")


def test_get_sheets_id_type_data():
    """
    test_get_sheets_id_type_data checks every id sheet is integer
    """
    print("\n" + test_get_sheets_id_type_data.__name__)
    res = client.get(ENDPOINT)
    assert all(isinstance(sheet['id'], int) for sheet in res.get_json()["Sheets"]) is True, "column 'id' not int"
    print("–    All \"id\" sheets have type of data \"int\"")


def test_get_sheets_title_type_data():
    """
    test_get_sheets_title_type_data checks every title sheet is string/text
    """
    print("\n" + test_get_sheets_title_type_data.__name__)
    res = client.get(ENDPOINT)
    assert all(isinstance(sheet['title'], str) for sheet in res.get_json()["Sheets"]) is True, "column 'title' not str"
    print("–    All \"title\" sheets have type of data \"str\"")


# ------------------------------------------------
# test def get_necessary_sheet
def test_get_necessary_sheet():
    """
    test_get_necessary_sheet checks status code 200 while url ENDPOINT(detail in file settings.py) + '<sheet_title>'
    """
    print("\n" + test_get_necessary_sheet.__name__)
    sheet_name = "Test_sheet"
    res = client.get(ENDPOINT + sheet_name, method=['GET'])
    # Checks that def work is ok
    assert res.status_code == 200, "cells of sheet are missing"
    print("–   " + ENDPOINT + "+'<sheet_title>' has status code - 200")


def test_get_necessary_wrong_sheet():
    """
    test_get_necessary_wrong_sheet checks status code 404 while url ENDPOINT(detail in file settings.py)
    + '<sheet_wrong_title>'
    """
    print("\n" + test_get_necessary_sheet.__name__)
    sheet_name = "Test_wrong_sheet"
    res = client.get(ENDPOINT + sheet_name, method=['GET'])
    # Checks that def work is ok
    assert res.status_code == 404, "cells of sheet are creating"
    print("–   " + ENDPOINT + "+'<sheet_title>' has status code - 404")


# ------------------------------------------------
# test def get_necessary_sheet
def test_get_necessary_sheet_cell():
    """
    test_get_necessary_sheet checks status code 200 while url
    ENDPOINT(detail in file settings.py) + '<sheet_title>' + '<cell_name>'
    """
    print("\n" + test_get_necessary_sheet_cell.__name__)
    sheet_name = "Test_sheet/"
    cell_name = "var1/"
    res = client.get(ENDPOINT + sheet_name + cell_name, method=['GET'])
    # Checks that def work is ok
    assert res.status_code == 200, "cell of sheet is missing"
    print("–   " + ENDPOINT + "+'<sheet_title>' + '<cell_name>' has status code - 200")


def test_get_necessary_wrong_sheet_cell():
    """
    test_get_necessary_sheet checks status code 404 while url
    ENDPOINT(detail in file settings.py) + '<sheet_wrong_title>' + '<cell_name>'
    """
    print("\n" + test_get_necessary_wrong_sheet_cell.__name__)
    sheet_name = "Test_wrong_sheet/"
    cell_name = "var1/"
    res = client.get(ENDPOINT + sheet_name + cell_name, method=['GET'])
    # Checks that def work is ok
    assert res.status_code == 404, "sheet is creating"
    print("–   " + ENDPOINT + "+'<sheet_wrong_title>' + '<sheet_title>' has status code - 404")


def test_get_necessary_sheet_wrong_cell():
    """
    test_get_necessary_sheet checks status code 404 while url
    ENDPOINT(detail in file settings.py) + '<sheet_title>' + '<cell_wrong_name>'
    """
    print("\n" + test_get_necessary_sheet_wrong_cell.__name__)
    sheet_name = "Test_sheet/"
    cell_name = "wrong_var1/"
    res = client.get(ENDPOINT + sheet_name + cell_name, method=['GET'])
    # Checks that def work is ok
    assert res.status_code == 404, "wrong is creating"
    print("–   " + ENDPOINT + "+'<sheet_title>' + '<sheet_wrong_title>' has status code - 404")


def test_get_necessary_wrong_sheet_wrong_cell():
    """
    test_get_necessary_sheet checks status code 404 while url
    ENDPOINT(detail in file settings.py) + '<sheet_wrong_title>' + '<cell_wrong_name>'
    """
    print("\n" + test_get_necessary_wrong_sheet_wrong_cell.__name__)
    sheet_name = "Test_wrong_sheet/"
    cell_name = "wrong_wrong_var1/"
    data_of_cell = (b"{\"value\": \"value1_test\",\"result\": \"value1_test\"}")
    res = client.get(ENDPOINT + sheet_name + cell_name, method=['GET'])
    res.set_data(data_of_cell)
    # Checks that def work is ok
    assert res.status_code == 404, "wrong is creating"
    print("–   " + ENDPOINT + "+'<sheet_wrong_title>' + '<sheet_wrong_title>' has status code - 404")