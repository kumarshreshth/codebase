#this module perform the function of migration updating data to different sheet as per user need
import columnsearch_module
import serialnumber_module


def migration(workbook, sheetindex, sheet_number, position, username_column, password_column, emailaddress_column, phonenumber_column, serialnumber_column):
    worksheet=workbook[sheetindex[sheet_number]]
    serialnumber_module.serialnumber_migration(serialnumber_column, worksheet, position)
    username_copy = worksheet.cell(row = position, column = username_column).value
    password_copy = worksheet.cell(row = position, column = password_column).value
    emailaddress_copy = worksheet.cell(row = position, column = emailaddress_column).value
    phonenumber_copy = worksheet.cell(row = position, column = phonenumber_column).value
    worksheet.delete_rows(position)
    print("data is deleted from sheet "+ sheetindex[sheet_number])


    if sheet_number == 0:
        sheet_number = 1
        worksheet = workbook[sheetindex[sheet_number]]
        password_column = columnsearch_module.passwordcolumnsearch(worksheet)
        username_column = columnsearch_module.usernamecolumnsearch(worksheet)
        emailaddress_column = columnsearch_module.emailaddresscolumnsearch(worksheet)
        phonenumber_column = columnsearch_module.phonenumbersearch(worksheet)
        serialnumber_column = columnsearch_module.serialnumber_search(worksheet)
        rowmax = worksheet.max_row
        serialnumber_module.serialnumber_migration_sheetchange(serialnumber_column, worksheet)
        username_paste = worksheet.cell(row = rowmax+1, column = username_column)
        username_paste.value = username_copy
        password_paste = worksheet.cell(row = rowmax+1, column = password_column)
        password_paste.value = password_copy
        emailaddress_paste = worksheet.cell(row = rowmax+1,column = emailaddress_column)
        emailaddress_paste.value = emailaddress_copy
        phonenumber_paste = worksheet.cell(row = rowmax+1, column = phonenumber_column)
        phonenumber_paste.value = phonenumber_copy
        print("data is shifted to sheet "+sheetindex[sheet_number])

    
    elif sheet_number == 1:
        sheet_number = 0
        worksheet = workbook[sheetindex[sheet_number]]
        password_column = columnsearch_module.passwordcolumnsearch(worksheet)
        username_column = columnsearch_module.usernamecolumnsearch(worksheet)
        emailaddress_column = columnsearch_module.emailaddresscolumnsearch(worksheet)
        phonenumber_column = columnsearch_module.phonenumbersearch(worksheet)
        serialnumber_column = columnsearch_module.serialnumber_search(worksheet)
        rowmax = worksheet.max_row
        serialnumber_module.serialnumber_migration_sheetchange(serialnumber_column, worksheet)
        username_paste = worksheet.cell(row = rowmax+1, column = username_column)
        username_paste.value = username_copy
        password_paste = worksheet.cell(row = rowmax+1, column = password_column)
        password_paste.value = password_copy
        emailaddress_paste = worksheet.cell(row = rowmax+1, column = emailaddress_column)
        emailaddress_paste.value = emailaddress_copy
        phonenumber_paste = worksheet.cell(row = rowmax+1, column = phonenumber_column)
        phonenumber_paste.value = phonenumber_copy
        print("data is shifted to sheet "+sheetindex[sheet_number])
