ЗАМЕТКА:
1) К сожалению, я допустил ошибку с тем, что при вычисление result нужно было идти от известных переменных (где в формуле нет ссылки на другие переменных) до менее известных. Тоесть, если var1= 1, var2 = var1+1, var3=var1+var2, то при вычисление var3  нужно было сначала записать result var1 потом result var2 и только потом result var3. К сожалению, времени исправить уже нет. Если это критично, то ладно, спасибо за хорошее задание, я много чего нового выучил)
2) 

**Description of input data:**
1) "GET /" or "GET /api/v1/"
   1) 200 if sheets are present
   2) 404 if sheets aren't created
   <br/>
   Example:
      * GET /api/v1/
        <br/>
        Response: {"Sheets":[{"id":1,"title":"Sheet1"},{"id":2,"title":"Sheet2"}]
2) GET /api/v1/:sheet_id or GET /api/v1/:sheet_id/ 
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
3) GET /api/v1/:sheet_id/:cell_id or GET /api/v1/:sheet_id/:cell_id/ 
   1) 200 if the value present
   2) 404 if the value is missing
          <br/>

          Examples:
           GET /api/v1/devchallenge-xx/var1 
           Response: {“value”: “1”, result: “1”} 
           GET /api/v1/devchallenge-xx/var1 
           Response: {“value”: “2”, result: “2”} 
           GET /api/v1/devchallenge-xx/var3 
           Response: {“value”: “=var1+var2”, result: “3”}
   
   4)  POST /api/v1/:sheet_id/ accept params {“title”: “1”} implements UPSERT strategy (update or insert) for both sheet_id
      1) 201 if the title sheet is OK
      2) 422 if the title sheet is not OK e.g. new title sheet is not suitable (read https://support.microsoft.com/ru-ru/office/%D0%BF%D0%B5%D1%80%D0%B5%D0%B8%D0%BC%D0%B5%D0%BD%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BB%D0%B8%D1%81%D1%82%D0%B0-3f1f7148-ee83-404d-8ef0-9ff99fbad1f9#:~:text=%D0%92%D0%B0%D0%B6%D0%BD%D0%BE%3A%20%D0%98%D0%BC%D0%B5%D0%BD%D0%B0%20%D0%BB%D0%B8%D1%81%D1%82%D0%BE%D0%B2%20%D0%BD%D0%B5%20%D0%BC%D0%BE%D0%B3%D1%83%D1%82,%D0%A1%D0%BE%D0%B4%D0%B5%D1%80%D0%B6%D0%B0%D1%82%D1%8C%20%D0%B1%D0%BE%D0%BB%D0%B5%D0%B5%2031%20%D0%B7%D0%BD%D0%B0%D0%BA%D0%B0.&text=%D0%9D%D0%B0%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%80%2C%2002%2F17%2F2016,%2D17%2D2016%20%E2%80%94%20%D0%BC%D0%BE%D0%B6%D0%BD%D0%BE)
      3) Добавить лист: curl -X POST -H "Content-type: application/json" http://localhost:8000/api/v1/Test_sheet9544/ -d '{}'  
      4) Изменить название листу: curl -X POST -H "Content-type: application/json" http://localhost:8000/api/v1/Test_sheet/ -d '{"title": "Test_sheet_2"}'

      Examples:
      POST /api/v1/Sheet_test/
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
   POST /api/v1/Sheet_test/ with {“title:”: “Test_sheet18”}
         {
      "var1": {
        "value": "value1_test",
        "result": "value1_test"
      },
      "var2": {
        "value": "value2_test",
        "result": "value2_test"
      }

   4)  POST /api/v1/:sheet_id/:cell_id accept params {"name": "cell_name", "value": "1"} implements UPSERT strategy (update or insert) for both sheet_id
      1) 201 if the cell name and cell value is OK
      2) 422 if the cell name or cell value is not OK e.g. new cell name or cell value is not suitable (read https://support.microsoft.com/en-gb/office/use-a-screen-reader-to-name-a-cell-or-data-range-in-excel-e8b55e7a-2cfd-40c4-9ea9-e738aa24e32c
)
   3) 409 if the new cell name has already been created until request
      3) Добавить новую ячейку: curl -X POST -H "Content-type: application/json" http://localhost:8000/api/v1/Test_sheet/var1 -d '{}
   4) Изменить название ячейки без value: curl -X POST -H "Content-type: application/json" http://localhost:8000/api/v1/Test_sheet/var1 -d '{"name":"name_new"} 
   5) Изменить название ячейки с value: curl -X POST -H "Content-type: application/json" http://localhost:8000/api/v1/Test_sheet/var1 -d '{"name":"name_new", "value":"value_new"} 
   6) Изменить value : curl -X POST -H "Content-type: application/json" http://localhost:8000/api/v1/Test_sheet/var1 -d '{"value":"value_new"}


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

1) test_get_necessary_sheet_cell -- checks status code 200 while url ENDPOINT(detail in file settings.py) + '<sheet_title>' + '<cell_name>'
2) test_get_necessary_wrong_sheet_cell -- checks status code 404 while url ENDPOINT(detail in file settings.py) + '<sheet_wrong_title>' + '<cell_name>'
3) test_get_necessary_sheet_wrong_cell -- checks status code 404 while url  ENDPOINT(detail in file settings.py) + '<sheet_title>' + '<cell_wrong_name>'
4) test_get_necessary_wrong_sheet_wrong_cell -- checks status code 404 while url ENDPOINT(detail in file settings.py) + '<sheet_wrong_title>' + '<cell_wrong_name>'

**Тесты: "POST /api/v1/:sheet_id" with {“title”: “Test_sheep”} implements UPSERT strategy (update or insert) for both sheet_id**

1) test_post_sheet -- checks change old title to a new title
2) test_post_sheet_not_exist_title -- checks change if old title not exist
3) test_post_sheet_not_json_title -- checks POST json not has 'title'
4) test_post_sheet_not_json_title -- checks POST json has 'title' but it is ""
5) test_post_sheet_wrong_len_name_32_and_more -- checks POST json has len 'title' =>32
6) test_post_sheet_wrong_name_contains_slash -- checks POST json has 'title' and it contains '\'
7) test_post_sheet_wrong_name_contains_colon_question_mark -- checks POST json has 'title' and it contains '?'
8) test_post_sheet_wrong_name_contains_asterisk_sign -- checks POST json has 'title' and it contains '*'
9) test_post_sheet_wrong_name_contains_colon_sign -- checks POST json has 'title' and it contains ':'
10) test_post_sheet_wrong_name_contains_colon_closing_parenthesis_right -- checks POST json has 'title' and it contains '['
11) test_post_sheet_wrong_name_contains_colon_closing_parenthesis_left -- checks POST json has 'title' and it contains ']'
12) test_post_sheet_wrong_name_as_History checks POST json has 'title' -- and it is 'History'

**Тесты: "POST /api/v1/:sheet_id/:cell_id accept params {“value”: “1”} implements UPSERT strategy (update or insert) for both sheet_id and cell_id"**

1) test_post_new_cell_new_value -- checks change new cell to a new title and new value 
2) test_post_cell_wrong_name_no_english checks POST json hasn't non english letters 
3) test_post_cell_wrong_name_as_gap -- checks POST json hasn't gas 
4) test_insert_post_new_already_exits_cell -- checks POST json hasn't new value and new name 
5) test_post_new_cell_without_new_value checks POST --  json hasn't new value 
6) test_post_new_value_without_name checks -- POST json hasn't new name cell

** Тесты формул **
1) test_post_new_value_with_simply_formula -- checks formula "=1"
2) test_post_new_value_with_hard_formula -- checks formula "=((var2-(var3+var2))*var2)*(var3+var2)"
3) test_post_new_value_without_formula -- checks value 1
4) test_post_value_self_name -- checks formula "=var1"
5) test_post_value_wrong_name -- checks formula  "=var1"
6) test_post_value_wrong_symbols -- checks formula "=var1+&%"
7) test_post_value_two_more_equal_sign -- checks formula "=var1+=var"

command:
curl -X POST -H "Content-type: application/json" http://localhost:8000/api/v1/Test_sheet1/ -d '{"value": "0"}'

curl http://localhost:8000/api/v1/Test_sheet/

pytest tests_views.py -s

 curl -X POST -H "Content-type: application/json" http://localhost:8000/api/v1/Test_sheet/var1 -d '{"name": "zrada", "value":""}'

 curl -X POST -H "Content-type: a
pplication/json" http://localhost:8000/api/v1/Test_sheet/var1 -d '{ "value":"=((var2-(var3+var2))*var2)*(var3+var2)"}'
