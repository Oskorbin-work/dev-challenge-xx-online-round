**Description of input data:**
1) "GET /" or "GET /api/v1/"
   1) 200 if sheets are present
   2) 404 if sheets aren't created
   <br/>
   Example:
      * GET /api/v1/
        <br/>
        Response: {"Sheets":[{"id":1,"title":"Sheet1"},{"id":2,"title":"Sheet2"}]
2) GET /api/v1/:sheet_id
   1) 200 if the sheet is present
   2) 404 if the sheet is missing
   <br/>
   Example:
   {
  "var1": {
    "value": "value1_test",
    "result": "value1_test"
  },
  "var2": {
    "value": "value2_test",
    "result": "value2_test"
  }
}


**Тесты: "GET /" or "GET /api/v1/"**
1) test_get_sheets -- checks status code 200 while url ENDPOINT(detail in file settings.py)
2) test_get_sheets_check_key_sheets -- checks key Sheets in Sheets exist
3) test_get_sheets_check_key_value_sheets -- checks key Sheets in Sheets is list
4) test_get_sheets_check_key_value_sheets_contain_dict -- checks every sheet is dict.
5) test_get_sheets_count_columns -- checks dict every sheet has two columns. 
6) test_get_sheets_has_id --checks every id sheet is exits.
7) test_get_sheets_has_title -- checks every title sheet is exist.
8) test_get_sheets_id_type_data -- checks every id sheet is integer.
9) test_get_sheets_title_type_data -- checks every title sheet is integer.

**Тесты:  "GET /api/v1/:sheet_id" or "GET /api/v1/:sheet_id/"**

_Заметки: sheet_wrong_title is wrong sheet._ 

1) test_get_sheets -- checks status code 200 while url ENDPOINT(detail in file settings.py) + '<sheet_title>'
2) test_get_necessary_wrong_sheet -- checks status code 404 while url ENDPOINT(detail in file settings.py)
+ '<sheet_wrong_title>' 

**Тесты: "GET /api/v1/:sheet_id/:cell_id" or "/api/v1/:sheet_id/:cell_id/"**

_Заметки: sheet_wrong_title is wrong sheet. cell_wrong_title is wrong cell of sheet._ 

1) test_get_necessary_sheet_cell -- checks status code 200 while url
    ENDPOINT(detail in file settings.py) + '<sheet_title>' + '<cell_name>'
2) test_get_necessary_wrong_sheet_cell -- checks status code 404 while url
    ENDPOINT(detail in file settings.py) + '<sheet_wrong_title>' + '<cell_name>'
3) test_get_necessary_sheet_wrong_cell -- checks status code 404 while url
    ENDPOINT(detail in file settings.py) + '<sheet_title>' + '<cell_wrong_name>'
4) test_get_necessary_wrong_sheet_wrong_cell -- checks status code 404 while url
    ENDPOINT(detail in file settings.py) + '<sheet_wrong_title>' + '<cell_wrong_name>'
