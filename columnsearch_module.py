#this module search where the main column exist

def passwordcolumnsearch(worksheet):
    for password_column in range(1, worksheet.max_column + 1):
        element = worksheet.cell(row=1, column = password_column)
        if element.value == "PASSWORD":
            break
    return password_column

def usernamecolumnsearch(worksheet):
    for username_column in range(1, worksheet.max_column + 1):
        element = worksheet.cell(row=1, column= username_column)
        if element.value == "USERNAME":
            break
    return username_column

def emailaddresscolumnsearch(worksheet):
    for emailaddress_column in range(1, worksheet.max_column + 1):
        element = worksheet.cell(row=1, column= emailaddress_column)
        if element.value == "EMAIL ADDRESS":
            break
    return emailaddress_column

def phonenumbersearch(worksheet):
    for phonenumber_column in range(1, worksheet.max_column + 1):
        element = worksheet.cell(row = 1 , column = phonenumber_column)
        if element.value == "PHONE NUMBER":
            break
    return phonenumber_column

def serialnumber_search(worksheet):
    for serialnumber_column in range(1, worksheet.max_column + 1):
        element = worksheet.cell(row = 1, column = serialnumber_column)
        if element.value == "S.No":
            break
    return serialnumber_column
