""" This code executes:
    a) tests
"""
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


def test_get_necessary_wrong_sheet_wrong_cell():
    """
    test_get_necessary_sheet checks status code 404 while url
    ENDPOINT(detail in file settings.py) + '<sheet_wrong_title>' + '<cell_wrong_name>'
    """
    print("\n" + test_get_necessary_wrong_sheet_wrong_cell.__name__)
    sheet_name = "Test_wrong_sheet/"
    cell_name = "wrong_wrong_var/"
    data_of_cell = (b"{\"value\": \"value1_test\",\"result\": \"value1_test\"}")
    res = client.get(ENDPOINT + sheet_name + cell_name, method=['GET'])
    res.set_data(data_of_cell)
    # Checks that def work is ok
    assert res.status_code == 404, "wrong is creating"
    print("–   " + ENDPOINT + "+'<sheet_wrong_title>' + '<sheet_wrong_title>' has status code - 404")


# ------------------------------------------------
# test def post_necessary_sheet

def test_post_sheet():
    """
    test_post_sheet checks change old title to a new title
    """
    print("\n" + test_post_sheet.__name__)
    data = {
        "title": "zrada"
    }
    res = client.post(ENDPOINT+"Test_sheet/", json=data)
    assert res.status_code == 200, "not changes title sheet"
    data = {
        "title": "Test_sheet"
    }
    res = client.post(ENDPOINT+"zrada/", json=data)
    assert res.status_code == 200, "not changes title sheet"


def test_post_sheet_not_exist_title():
    """
    test_post_sheet_not_exist_title checks change if old title not exist
    """
    print("\n" + test_post_sheet_not_exist_title.__name__)
    data = {
        "title": "zrada"
    }
    res = client.post(ENDPOINT+"Test_sheet434345/", json=data)
    assert res.status_code == 404, "finds not exist sheet"


def test_post_sheet_not_json_title():
    """
     test_post_sheet_not_json_title checks POST json not has 'title'
    """
    print("\n" + test_post_sheet_not_json_title.__name__)
    data = {
        "title1": "zrada"
    }
    res = client.post(ENDPOINT+"Test_sheet/", json=data)
    assert res.status_code == 422, "wrong with post json. title1 is not title"


def test_post_sheet_wrong_name_as_empty():
    """
     test_post_sheet_not_json_title checks POST json has 'title' but it is ""
    """
    print("\n" + test_post_sheet_wrong_name_as_empty.__name__)
    data = {
        "title": ""
    }
    res = client.post(ENDPOINT+"Test_sheet/", json=data)
    assert res.status_code == 422, "post json 'title' is empty"


def test_post_sheet_wrong_len_name_32_and_more():
    """
      test_post_sheet_wrong_len_name_32_and_more checks POST json has len 'title' =>32
     """
    print("\n" + test_post_sheet_wrong_len_name_32_and_more.__name__)
    data = {
        "title": "bnflmnbklfnbkfdlxbfgnmhdl;ckxmbnlfgdmgklbnfjgkldgjvmb jfglkndmcxvbnfjgidpolkvjbnfgkdlngvbfj"
    }
    res = client.post(ENDPOINT + "Test_sheet/", json=data)
    assert res.status_code == 422, "len title not has len =>32"


def test_post_sheet_wrong_name_contains_slash():
    """
      test_post_sheet_wrong_name_contains_slash checks POST json has 'title' and it contains '\'
     """
    print("\n" + test_post_sheet_wrong_name_contains_slash.__name__)
    data = {
        "title": "/title"
    }
    res = client.post(ENDPOINT + "Test_sheet/", json=data)
    assert res.status_code == 422, " title not has symbols /"


def test_post_sheet_wrong_name_contains_colon_question_mark():
    """
      test_post_sheet_wrong_name_contains_colon_question_mark checks POST json has 'title' and it contains '?'
     """
    print("\n" + test_post_sheet_wrong_name_contains_colon_question_mark.__name__)
    data = {
        "title": "?title"
    }
    res = client.post(ENDPOINT + "Test_sheet/", json=data)
    assert res.status_code == 422, " title not has symbols ?"


def test_post_sheet_wrong_name_contains_asterisk_sign():
    """
      test_post_sheet_wrong_name_contains_asterisk_sign checks POST json has 'title' and it contains '*'
     """
    print("\n" + test_post_sheet_wrong_name_contains_asterisk_sign.__name__)
    data = {
        "title": "*title"
    }
    res = client.post(ENDPOINT + "Test_sheet/", json=data)
    assert res.status_code == 422, " title not has symbols *"


def test_post_sheet_wrong_name_contains_colon_sign():
    """
      test_post_sheet_wrong_name_contains_colon_sign checks POST json has 'title' and it contains ':'
     """
    print("\n" + test_post_sheet_wrong_name_contains_colon_sign.__name__)
    data = {
        "title": "ti:tle"
    }
    res = client.post(ENDPOINT + "Test_sheet/", json=data)
    assert res.status_code == 422, " title not has symbols :"


def test_post_sheet_wrong_name_contains_colon_closing_parenthesis_right():
    """
      test_post_sheet_wrong_name_contains_colon_closing_parenthesis_right checks POST json has 'title' and it contains '['
     """
    print("\n" + test_post_sheet_wrong_name_contains_colon_closing_parenthesis_right.__name__)
    data = {
        "title": "[title"
    }
    res = client.post(ENDPOINT + "Test_sheet/", json=data)
    assert res.status_code == 422, " title not has symbols ["


def test_post_sheet_wrong_name_contains_colon_closing_parenthesis_left():
    """
      test_post_sheet_wrong_name_contains_colon_closing_parenthesis_left checks POST json has 'title' and it contains ']'
     """
    print("\n" + test_post_sheet_wrong_name_contains_colon_closing_parenthesis_left.__name__)
    data = {
        "title": "tit]le"
    }
    res = client.post(ENDPOINT + "Test_sheet/", json=data)
    assert res.status_code == 422, " title not has symbol ]"


def test_post_sheet_wrong_name_as_History():
    """
      test_post_sheet_wrong_name_as_History checks POST json has 'title' and it is 'History'
     """
    print("\n" + test_post_sheet_wrong_name_as_History.__name__)
    data = {
        "title": "History"
    }
    res = client.post(ENDPOINT + "Test_sheet/", json=data)
    assert res.status_code == 422, " title not has name as 'History'"

# ------------------------------------------------
# test def post_necessary_cell


def test_post_new_cell_new_value():
    """
      test_post_new_cell_new_value checks change new cell to a new title and new value
     """
    print("\n" + test_post_new_cell_new_value.__name__)
    data = {
        "name": "zrada",
        "value": "test_value"
    }
    res = client.post(ENDPOINT+"Test_sheet/var1/", json=data)

    assert res.status_code == 200, "not changes name cell with a new value"
    data = {
        "name": "var1",
        "value": ""
    }
    res = client.post(ENDPOINT+"Test_sheet/zrada/", json=data)
    assert res.status_code == 200, "not changes name cell with a new value"


def test_post_cell_wrong_name_no_english():
    """
      test_post_cell_wrong_name_no_english checks POST json hasn't non english letters
     """
    print("\n" + test_post_cell_wrong_name_no_english.__name__)
    data = {
        "name": "ФБФ",
        "value": "test_value"
    }
    res = client.post(ENDPOINT+"Test_sheet/var1/", json=data)
    assert res.status_code == 422, "not changes name cell with a new value"


def test_post_cell_wrong_name_as_gap():
    """
      test_post_cell_wrong_name_as_gap checks POST json hasn't gas
     """
    print("\n" + test_post_cell_wrong_name_as_gap.__name__)
    data = {
        "name": "Test Test",
        "value": "test_value"
    }
    res = client.post(ENDPOINT+"Test_sheet/var1/", json=data)
    assert res.status_code == 422, "add wrong name cell (gap inside)"
    data = {
        "name": "Test_Test ",
        "value": "test_value"
    }
    res = client.post(ENDPOINT+"Test_sheet/var1/", json=data)
    assert res.status_code == 422, "add wrong name cell (gap left)"
    data = {
        "name": " Test_Test",
        "value": "test_value"
    }
    res = client.post(ENDPOINT+"Test_sheet/var1/", json=data)
    assert res.status_code == 422, "add wrong name cell (right)"


def test_insert_post_new_already_exits_cell():
    """
      test_insert_post_new_already_exits_cell checks POST json hasn't new value and new name
     """
    print("\n" + test_insert_post_new_already_exits_cell.__name__)
    data = {}
    res = client.post(ENDPOINT+"Test_sheet/var1/", json=data)
    assert res.status_code == 409, "add the new cell name has already been created until request"


def test_post_new_cell_without_new_value():
    """
      test_post_new_cell_without_new_value checks POST json hasn't new value
     """
    print("\n" + test_post_new_cell_without_new_value.__name__)
    data = {
        "name": "zrada"
    }
    res = client.post(ENDPOINT+"Test_sheet/var1/", json=data)
    assert res.status_code == 200, "wrong without new value"
    data = {
        "name": "var1"
    }
    res = client.post(ENDPOINT+"Test_sheet/zrada/", json=data)
    assert res.status_code == 200, "wrong without new value"


def test_post_new_value_without_name():
    """
      test_post_new_value_without_name checks POST json hasn't new name cell
     """
    print("\n" + test_post_new_value_without_name.__name__)
    data = {
        "value": "zrada"
    }
    res = client.post(ENDPOINT+"Test_sheet/var1/", json=data)

    assert res.status_code == 200, "wrong without name"
    data = {
        "value": ""
    }
    res = client.post(ENDPOINT+"Test_sheet/var1/", json=data)

    assert res.status_code == 200, "wrong without name"

# ------------------------------------------------
# test formula

def test_post_new_value_with_simply_formula():
    """
      test_post_new_value_with_simply_formula checks formula "=1"
     """
    print("\n" + test_post_new_value_with_simply_formula.__name__)
    data = {
        "value": "=1"
    }
    res = client.post(ENDPOINT+"Test_sheet/var1/", json=data)

    assert res.status_code == 200, "wrong without formula"


def test_post_new_value_with_hard_formula():
    """
      test_post_new_value_with_hard_formula checks formula "=((var2-(var3+var2))*var2)*(var3+var2)"
     """
    print("\n" + test_post_new_value_with_hard_formula.__name__)
    data = {
        "value": "=((var2-(var3+var2))*var2)*(var3+var2)"
    }
    res = client.post(ENDPOINT+"Test_sheet/var1/", json=data)
    assert res.status_code == 200, "wrong formula"


def test_post_new_value_without_formula():
    """
      test_post_new_value_without_formula checks value 1
     """
    print("\n" + test_post_new_value_without_name.__name__)
    data = {
        "value": "1"
    }
    res = client.post(ENDPOINT+"Test_sheet/var1/", json=data)

    assert res.status_code == 200, "wrong without formula"


def test_post_value_self_name():
    """
      test_post_value_self_name checks formula "=var1"
     """
    print("\n" + test_post_value_self_name.__name__)
    data = {
        "value": "=var1"
    }
    res = client.post(ENDPOINT+"Test_sheet/var1/", json=data)

    assert res.status_code == 422, "self name can not in the formula"


def test_post_value_wrong_name():
    """
      test_post_value_wrong_name checks formula  "=var1"
     """
    print("\n" + test_post_value_wrong_name.__name__)
    data = {
        "value": "=var1"
    }
    res = client.post(ENDPOINT+"Test_sheet/var1/", json=data)

    assert res.status_code == 422, "self name can not in the formula"


def test_post_value_wrong_symbols():
    """
      test_post_value_wrong_symbols checks formula "=var1+&%"
     """
    print("\n" + test_post_value_wrong_name.__name__)
    data = {
        "value": "=var1+&%"
    }
    res = client.post(ENDPOINT+"Test_sheet/var1/", json=data)

    assert res.status_code == 422, "wrong symbols can not in the formula"


def test_post_value_two_more_equal_sign():
    """
      test_post_value_two_more_equal_sign checks formula "=var1+=var"
     """
    print("\n" + test_post_value_two_more_equal_sign.__name__)
    data = {
        "value": "=var1+=var"
    }
    res = client.post(ENDPOINT+"Test_sheet/var1/", json=data)

    assert res.status_code == 422, "two_more_equal_sign can not in the formula"
