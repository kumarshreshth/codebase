#this module tells whether the userid already exist or not and the perform action based on choice
import mirgration_module as mg
import fetch_module as fm
import update_module

def existence(username,worksheet,username_column,password_column,emailaddress_column,phonenumber_column, workbook,sheetindex,sheet_number, serialnumber_column):
    check_existence = False
    for position in range(1, worksheet.max_row+1):
        value_cell = worksheet.cell(row= position, column= username_column).value
        if value_cell == username:
            old_password = worksheet.cell(row = position, column = password_column).value
            check_existence = True
            print("Entered userid already exist in "+ sheetindex[sheet_number]+ " sheet")
            while True :
                print("enter 1 to update details " + "\nenter 2 to fetch details "+"\nenter 3 to migrate user"+"\nenter 4 to exit")
                choice = input()

                if choice == "2":
                    fm.fetch_data(position, username_column, password_column, emailaddress_column, phonenumber_column, worksheet)

                if choice == "1":
                    update_module.update_details(position, password_column, emailaddress_column, phonenumber_column, worksheet, username, old_password)
                
                if choice == "3":
                    mg.migration(workbook, sheetindex, sheet_number, position, username_column, password_column, emailaddress_column, phonenumber_column, serialnumber_column)
                    break
                
                if choice == "4" or choice == "":
                    break
                
                else:
                    break
                print('\n')
    
    return check_existence