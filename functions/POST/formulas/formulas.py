""" This code executes:
1) check value (formula or text)
2) get new result
"""
# Import python Modules
import regex
# Import flask Modules
from flask import abort
# Import project Modules
from database.requests import get_all_cells_of_necessary_sheet, get_necessary_sheet_cell
from functions.POST.formulas.calculator import RPN


def get_list_math_operations():
    """
     get_list_math_operations contains a math operations
    :return: math operations
    """
    return ["+", "-", "/", "*", "(", ")"]


def get_list_all_name_cells_sheet(sheet_title):
    """
    get_list_all_name_cells_sheet does get all necessary name cells
    :param sheet_title: title sheet
    :return: all cells of a necessary name cells
    """
    return {name['name'] for name in get_all_cells_of_necessary_sheet(sheet_title)}


def get_list_all_symbols(sheet_title):
    """
    get_list_all_symbols does get all symbols value
    :param sheet_title: title sheet
    :return: all symbols value
    """
    zrada =set()
    for i in get_list_all_name_cells_sheet(sheet_title):
        for j in str(i):
            zrada.update([j])
    zrada.update(get_list_math_operations())
    return zrada


def get_list_all_name_formula(value):
    """
    get_list_all_symbols does get all name formula
    :param value: value of cell
    :return: all name formula
    """
    reg = rf'(?<=[\+-\/*()\s]|^)[a-z|\d|^\s]*(?=[\+-\/*()\s]|$)'
    search_names = set()
    for m in regex.finditer(reg, value):
        if m.group(0).isnumeric():
            pass
        else:
            search_names.add(m.group(0))
    if "" in search_names:
        search_names.remove("")
    return search_names


def get_value_formula(value, name_cell, name_sheet):
    """
    get_value_formula get formula
    :param value: value of cell
    :param name_cell: cell name
    :param name_sheet: title sheet
    :return: formula or value
    """
    if check_is_formula(value) is False:
        return value
    else:
        value = value[1:]
    check_error(value, name_cell, name_sheet)
    result = get_result(value,name_sheet)
    return result


def check_is_formula(value):
    """
    check_is_formula check formula
    :param value: value of cell
    :return: True formula. False is value
    """
    if value == "":
        return False
    if value[0] == "=":
        return True
    else:
        return False


def check_error(value, name_cell, name_sheet):
    """
    check_error check error formula
    :param value: value of cell
    :param name_cell: cell name
    :param name_sheet: title sheet
    :return: HTTP STATUS 422 or formula good
    """
    def check_self_name(value, name_cell):
        """
        check_self_name check formula not has self name cell
        :param value: value of cell
        :param name_cell: cell name
        :return: HTTP STATUS 422 or formula good
        """
        if len(check_name(value, name_cell)) == 0:
            pass
        else:
            abort(422)

    def check_exist_name(value,name_sheet):
        """
        check_self_name check formula has only exist name cell
        :param value: value of cell
        :param name_sheet: sheet cell
        :return: HTTP STATUS 422 or formula good
        """
        get_cell_sheet = get_list_all_name_cells_sheet(name_sheet)
        get_cell_value = get_list_all_name_formula(value)
        if get_cell_value == {}:
            pass
        elif get_cell_value.issubset(get_cell_sheet):
            pass
        else:
            abort(422)

    def check_all_symbols(value, name_sheet):
        """
        check_self_name check all symbols formula
        :param value: value of cell
        :param name_sheet: sheet cell
        :return: HTTP STATUS 422 or formula good
        """
        list_all_symbols = get_list_all_symbols(name_sheet)
        if set(value).issubset(list_all_symbols):
            pass
        else:
            abort(422)

    check_self_name(value, name_cell)
    check_exist_name(value, name_sheet)
    check_all_symbols(value, name_sheet)


def check_name(value, name_cell):
    """
    check_name get all names cell of formula
    :param value: value of cell
    :param name_cell: cell name
    :return: list of all names cell of formula
    """
    reg = rf'(?<=[\+-\/*()\s]|^)({name_cell})(?=[\+-\/*()\s]|$)'
    list_of_search_word = [m.group(0) for m in regex.finditer(reg, value)]
    return list_of_search_word


def get_result(value, name_sheet):
    """
     get_result get result cell
     :param value: value of cell
     :param name_sheet: name sheet
     :return: result
     """
    result = value
    list_all_name_formula = get_list_all_name_formula(value)
    for cell in list_all_name_formula:
        temp = get_necessary_sheet_cell(name_sheet, cell)[0]['result']
        if temp.isnumeric():
            result = result.replace(cell,temp)
        else:
            abort(422)
    list_of_symbols = get_list_math_operations()
    for char in list_of_symbols:
        result = result.replace(char, " "+char+" ")
    result = result.replace("  ", " ")
    if result[0] == " ":
        result = result[1:]
    if result[-1] == " ":
        result = result[:-1]
    rpn = RPN(result)
    rpn.check()
    rpn.postfix()
    try:
        result = rpn.calculate()
    except:
        abort(422)
    return result
