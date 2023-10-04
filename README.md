# List Of Contents
<!-- TOC -->
* [List Of Contents](#list-of-contents)
* [Description project](#description-project)
  * [Description](#description)
  * [Description of input data](#description-of-input-data)
  * [Requirements](#requirements)
* [Start Project](#start-project)
* [Run tests](#run-tests)
* [Note to projects (It is important):](#note-to-projects-it-is-important)
* [Description of input data](#description-of-input-data-1)
* [Test cases:](#test-cases)
  * ["GET /" or "GET /api/v1/"](#get--or-get-apiv1)
  * ["GET /api/v1/:sheet_id" or "GET /api/v1/:sheet_id/"](#get-apiv1sheetid-or-get-apiv1sheetid)
  * ["GET /api/v1/:sheet_id/:cell_id" or "/api/v1/:sheet_id/:cell_id/"](#get-apiv1sheetidcellid-or-apiv1sheetidcellid)
  * ["POST /api/v1/:sheet_id" with {“title”: “Test_sheep”} implements UPSERT strategy (update or insert) for both sheet_id](#post-apiv1sheetid-with-title-testsheep-implements-upsert-strategy-update-or-insert-for-both-sheetid)
  * ["POST /api/v1/:sheet_id/:cell_id accept params {“value”: “1”} implements UPSERT strategy (update or insert) for both sheet_id and cell_id"](#post-apiv1sheetidcellid-accept-params-value-1-implements-upsert-strategy-update-or-insert-for-both-sheetid-and-cellid)
  * ["Test of formula"](#test-of-formula)
<!-- TOC -->

# Description project

## Description

We all know there is no better software in the world than Excel 
The powerful idea behind the cells and formulas allows many of us to understand programming. 
Today is your time to pay respect to spreadsheets and implement backend API for this fantastic tool. 

## Description of input data

As a user, I want to have API service with exact endpoints:
POST /api/v1/:sheet_id/:cell_id accept params {“value”: “1”} implements UPSERT strategy (update or insert) for both sheet_id and cell_id
1) 201 if the value is OK
2) 422 if the value is not OK e.g. new value leads to dependent formula ERROR compilation
Examples:
POST /api/v1/devchallenge-xx/var1 with {“value:”: “0”}
Response: {“value:”: “0”, “result”: “0”}
POST /api/v1/devchallenge-xx/var1 with {“value:”: “1”}
Response: {“value:”: “1”, “result”: “1”}
POST /api/v1/devchallenge-xx/var2 with {“value”: “2”} 
Response: {“value:”: “2”, “result”: “2”}
POST /api/v1/devchallenge-xx/var3 with {“value”: “=var1+var2”}
Response: {“value”: “=var1+var2”, “result”: “3”}
POST /api/v1/devchallenge-xx/var4 with {“value”: “=var3+var4”}
Response: {“value”: “=var3+var4”, “result”: “ERROR”}

GET  /api/v1/:sheet_id/:cell_id
1) 200 if the value present
2) 404 if the value is missing
Examples:
GET /api/v1/devchallenge-xx/var1
Response: {“value”: “1”, result: “1”}
GET /api/v1/devchallenge-xx/var1
Response: {“value”: “2”, result: “2”}
GET /api/v1/devchallenge-xx/var3
Response: {“value”: “=var1+var2”, result: “3”}

GET /api/v1/:sheet_id
1) 200 if the sheet is present
2) 404 if the sheet is missing
Response:
{
“var1”: {“value”: “1”, “result”: “1”},
“var2”: {“value”: “2”, “result”: “2”},
“var3”: {“value”: “=var1+var2”, “result”: “3”}
}



## Requirements

Supports basic data types: string, integer, float
Support basic math operations like +, -, /, * and () as well.
:sheet_id - should be any URL-compatible text that represents the namespace and can be generated on the client
:cell_id - should be any URL-compatible text that represents a cell (variable) and can be generated on the client
:sheet_id and :cell_id are case-insensitive
Be creative and cover as many corner cases as you can. Please do not forget to mention them in the README.md
Data should be persisted and available between docker containers restarts

# Start Project
1. Go to the folder '**docker**' (as project root) which contains file docker-compose.py and folder Backend (contains project files);
2. You can type command "**docker-compose up**" or "**sudo docker-compose up**" into command line;
3. Open URl http://localhost:8080/api/v1/. You must see a list of sheets.
> If you open URl but you see error (maybe 'This site can’t be reached'), then you can open URL http://127.0.0.1:8080 .

# Run tests
You have two choices how you can run tests:
1) You can open URL http://localhost:8080/api/v1/tests/
2)  You can type command "pytest Backend/tests/tests_views.py -s"
 
 > Databases have the sheet "Test_sheet" and it the cell "var1". This is necessary to run tests. So it is better to not delete this sheet and cell.
 
# Note to projects (It is important):
 Unfortunately, I made a **_mistake_**. I don't have time to solve it. I’ll describe how it should be:
 - When project is calculating result of cell, It has to go to from known cells (Where value not contain other name of cell) to unknown cell.
 - Example:
 - We have cells: var1= 1, var2 = var1+1, var3=var1+var2
 - When project is  calculating var3, It is must give result var1, after result var2 и only then give result var3.
 
# Description of input data
 1) "GET /" or "GET /api/v1/"
 1) 200 if sheets are present
 2) 404 if sheets aren't created
 
 Example:
       * GET /api/v1/
 
     Response: 
 ```
     {"Sheets":[{"id":1,"title":"Sheet1"},{"id":2,"title":"Sheet2"}]
 ```
 
 2) GET /api/v1/:sheet_id or GET /api/v1/:sheet_id/
     1) 200 if the sheet is present
     2) 404 if the sheet is missing
 
 Example:
       * GET /api/v1/Sheet_Test
        Response:
 ```
     {
 "var1":{
       "value":"=1+2",
       "result":"3"
 },
 "var2":{
       "value":"=var1+1",
       "result":"4"
 }
     }
 ```
 3) GET /api/v1/:sheet_id/:cell_id or GET /api/v1/:sheet_id/:cell_id/
 1) 200 if the value present
 2) 404 if the value is missing
 
 Examples:
 
         GET /api/v1/devchallenge-xx/var1 
         Response: {“value”: “1”, result: “1”} 
         GET /api/v1/devchallenge-xx/var1 
         Response: {“value”: “2”, result: “2”} 
         GET /api/v1/devchallenge-xx/var3 
         Response: {“value”: “=var1+var2”, result: “3”}      
 
 4)  POST /api/v1/:sheet_id/ accept params {“title”: “1”} implements UPSERT strategy (update or insert) for both sheet_id
       1) 201 if the title sheet is OK
       2) 422 if the title sheet is not OK e.g. new title sheet is not suitable (read https://support.microsoft.com/en-us/office/rename-a-worksheet-3f1f7148-ee83-404d-8ef0-9ff99fbad1f9)
       3) Добавить лист: curl -X POST -H "Content-type: application/json" http://localhost:8000/api/v1/Test_sheet9544/ -d '{}'  
       4) Изменить название листу: curl -X POST -H "Content-type: application/json" http://localhost:8000/api/v1/Test_sheet/ -d '{"title": "Test_sheet_2"}'
       5) insert new sheet: 
     ```console
     curl -X POST -H "Content-type: application/json" http://localhost:8000/api/v1/Test_sheet -d '{}
     ```
       ```
 
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
       ```
       6) Update title sheet: 
     ```console
 curl -X POST -H "Content-type: application/json" http://localhost:8000/api/v1/Test_sheet/ -d '{"title":"Test_sheet18"}
      ```
 
       ```
          {
       "var1": {
         "value": "value1_test",
         "result": "value1_test"
       },
       "var2": {
         "value": "value2_test",
         "result": "value2_test"
       }
 ```
 
 5) POST /api/v1/:sheet_id/:cell_id accept params {"name": "cell_name", "value": "1"} implements UPSERT strategy (update or insert) for both sheet_id
       1) 201 if the cell name and cell value is OK
       2) 422 if the cell name or cell value is not OK e.g. new cell name or cell value is not suitable (read https://support.microsoft.com/en-gb/office/use-a-screen-reader-to-name-a-cell-or-data-range-in-excel-e8b55e7a-2cfd-40c4-9ea9-e738aa24e32c)
       3) 409 if the new cell name has already been created until request
       4) insert new cell: 
     ```console
     curl -X POST -H "Content-type: application/json" http://localhost:8000/api/v1/Test_sheet/var2 -d '{}
     ```
     ```
     {
 "name":"var2",
 "value":"1",
 "result":”1"
 }
     ```
 
       5) Update name cell without value: 
     ```console
 curl -X POST -H "Content-type: application/json" http://localhost:8000/api/v1/Test_sheet/var1 -d '{"name":"name_new"}
      ```
 ```
     {
 "name":"name_new",
 "value":"1",
 "result":"1"
 }
 ```
 6) Update name cell with value:
 ```console
 curl -X POST -H "Content-type: application/json" http://localhost:8000/api/v1/Test_sheet/var1 -d '{"name":"name_new", "value":"=1+2"}
 ```
 ```
     {
 "name":"name_new",
 "value":"=1+2",
 "result":"3"
 }
 ```
 7) update value of current cell :
 ```console   
 curl -X POST -H "Content-type: application/json" http://localhost:8000/api/v1/Test_sheet/var1 -d '{"value":"=1+2"}
 ```
 
 ```
     {
 "name":"var1",
 "value":"=1+2",
 "result":"3"
 }
 ```
 
 # Test cases:
 
 ## "GET /" or "GET /api/v1/"
 1) test_get_sheets -- checks status code 200 while url ENDPOINT(detail in file settings.py)
 2) test_get_sheets_check_key_sheets -- checks key Sheets in Sheets exist
 3) test_get_sheets_check_key_value_sheets -- checks key Sheets in Sheets is list
 4) test_get_sheets_check_key_value_sheets_contain_dict -- checks every sheet is dict.
 5) test_get_sheets_count_columns -- checks dict every sheet has two columns.
 6) test_get_sheets_has_id --checks every id sheet is exits.
 7) test_get_sheets_has_title -- checks every title sheet is exist.
 8) test_get_sheets_id_type_data -- checks every id sheet is integer.
 9) test_get_sheets_title_type_data -- checks every title sheet is integer.
 
 ## "GET /api/v1/:sheet_id" or "GET /api/v1/:sheet_id/"
 
 1) test_get_sheets -- checks status code 200 while url ENDPOINT(detail in file settings.py) + '<sheet_title>'
 2) test_get_necessary_wrong_sheet -- checks status code 404 while url ENDPOINT(detail in file settings.py)
 + '<sheet_wrong_title>'
 
 ## "GET /api/v1/:sheet_id/:cell_id" or "/api/v1/:sheet_id/:cell_id/"
 
 1) test_get_necessary_sheet_cell -- checks status code 200 while url ENDPOINT(detail in file settings.py) + '<sheet_title>' + '<cell_name>'
 2) test_get_necessary_wrong_sheet_cell -- checks status code 404 while url ENDPOINT(detail in file settings.py) + '<sheet_wrong_title>' + '<cell_name>'
 3) test_get_necessary_sheet_wrong_cell -- checks status code 404 while url  ENDPOINT(detail in file settings.py) + '<sheet_title>' + '<cell_wrong_name>'
 4) test_get_necessary_wrong_sheet_wrong_cell -- checks status code 404 while url ENDPOINT(detail in file settings.py) + '<sheet_wrong_title>' + '<cell_wrong_name>'
 
 ## "POST /api/v1/:sheet_id" with {“title”: “Test_sheep”} implements UPSERT strategy (update or insert) for both sheet_id
 
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
 
 ## "POST /api/v1/:sheet_id/:cell_id accept params {“value”: “1”} implements UPSERT strategy (update or insert) for both sheet_id and cell_id"
 
 1) test_post_new_cell_new_value -- checks change new cell to a new title and new value
 2) test_post_cell_wrong_name_no_english checks POST json hasn't non english letters
 3) test_post_cell_wrong_name_as_gap -- checks POST json hasn't gas
 4) test_insert_post_new_already_exits_cell -- checks POST json hasn't new value and new name
 5) test_post_new_cell_without_new_value checks POST --  json hasn't new value
 6) test_post_new_value_without_name checks -- POST json hasn't new name cell
 
 ## "Test of formula"
 
 1) test_post_new_value_with_simply_formula -- checks formula "=1"
 2) test_post_new_value_with_hard_formula -- checks formula "=((var2-(var3+var2))*var2)*(var3+var2)"
 3) test_post_new_value_without_formula -- checks value 1
 4) test_post_value_self_name -- checks formula "=var1"
 5) test_post_value_wrong_symbols -- checks formula "=var1+&%"
 6) test_post_value_two_more_equal_sign -- checks formula "=var1+=var"