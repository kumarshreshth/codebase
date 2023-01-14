# this module do the switching of sheet
import existence_module
import columnsearch_module

def switch_sheet(username, workbook, sheetindex, sheet_number):
    if sheet_number == 0:
        sheet_number = 1
        worksheet = workbook[sheetindex[sheet_number]]
        password_column = columnsearch_module.passwordcolumnsearch(worksheet)
        username_column = columnsearch_module.usernamecolumnsearch(worksheet)
        emailaddress_column = columnsearch_module.emailaddresscolumnsearch(worksheet)
        phonenumber_column = columnsearch_module.phonenumbersearch(worksheet)
        serialnumber_column = columnsearch_module.serialnumber_search(worksheet)
        check_existence = existence_module.existence(username, worksheet, username_column, password_column, emailaddress_column, phonenumber_column, workbook, sheetindex, sheet_number, serialnumber_column)
        return check_existence
    else:
        sheet_number = 0
        worksheet = workbook[sheetindex[sheet_number]]
        password_column = columnsearch_module.passwordcolumnsearch(worksheet)
        username_column = columnsearch_module.usernamecolumnsearch(worksheet)
        emailaddress_column = columnsearch_module.emailaddresscolumnsearch(worksheet)
        phonenumber_column = columnsearch_module.phonenumbersearch(worksheet)
        serialnumber_column = columnsearch_module.serialnumber_search(worksheet)
        check_existence = existence_module.existence(username, worksheet, username_column, password_column, emailaddress_column, phonenumber_column, workbook, sheetindex, sheet_number, serialnumber_column)
        return check_existence