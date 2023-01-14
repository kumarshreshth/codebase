# This is the main driver code
import openpyxl as op
import columnsearch_module
import newuser_module
import existence_module 
import userIDvadilation_module
import switch_sheet_module
import entry_module


workbook = op.load_workbook('database.xlsx')
workbook.active
sheetindex = []
sheetindex.extend(workbook.sheetnames)
while True:
    try:
        sheet = input("enter the usertype\n")
        worksheet = workbook[sheet]
        password_column = columnsearch_module.passwordcolumnsearch(worksheet)
        username_column = columnsearch_module.usernamecolumnsearch(worksheet)
        emailaddress_column = columnsearch_module.emailaddresscolumnsearch(worksheet)
        phonenumber_column = columnsearch_module.phonenumbersearch(worksheet)
        serialnumber_column = columnsearch_module.serialnumber_search(worksheet)
        choice = input("enter 1 to view all the entries in "+sheet+"\nenter 2 to input credentials yourself\n")
        if choice == "1":
            entry_module.all_entries(worksheet, username_column, password_column, emailaddress_column, phonenumber_column)
            break
        if choice == "2":
            if sheet == sheetindex[0]:
                sheet_number = 0
            if sheet == sheetindex[1]:
                sheet_number = 1
            username = input("enter the userid\n")
            message,status = userIDvadilation_module.userId_validition(username)
            if status == True:
                check_existence = existence_module.existence(username, worksheet, username_column, password_column, emailaddress_column, phonenumber_column, workbook, sheetindex, sheet_number, serialnumber_column)
                if check_existence == False:
                    checker = switch_sheet_module.switch_sheet(username, workbook, sheetindex, sheet_number)
                    if checker == False:
                        newuser_module.newuser(username, username_column, password_column, emailaddress_column, phonenumber_column, worksheet, serialnumber_column)
                workbook.save('database.xlsx')
            else:
                print(message)
            break
        else:
            print("incorrect choice")
            break

    except Exception as e :
        print(str(e))
        print(" press enter to try again")
        choice = input()
         
        if (choice) == "":
            continue

        else:
            break 