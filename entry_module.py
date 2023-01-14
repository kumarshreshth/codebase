# this module is used to print all entries in the sheet needed to be viewed by the user 
import maskpass


def all_entries(worksheet, username_column, password_column, emailaddress_column, phonenumber_column):
    security_key = "Project"
    user_input = maskpass.askpass(prompt = "enter the security key(only known if you are admin user)\n", mask = "#")
    print("\n")
    rowmax = worksheet.max_row
    dict = {}
    if user_input == security_key:
        for position in range(2, rowmax +1):
            list = []
            element_username = str(worksheet.cell(row = position, column = username_column).value)
            element_password = str(worksheet.cell(row = position, column = password_column).value)
            element_emailaddress = str(worksheet.cell(row = position, column = emailaddress_column).value)
            element_phonenumber = str(worksheet .cell (row = position, column = phonenumber_column).value)
            list.extend( [element_username, element_password, element_emailaddress, element_phonenumber])
            dict[position] = list
        print("{:10} {:40} {:40} {:40} {:40}".format('S.NO.','Username','Password','Email Address','Phone Number'))
        for key,value in dict.items():
            username, password, emailaddress, phonenumber = value
            print("{:10} {:40} {:40} {:40} {:40}".format(str(key-1), username, password, emailaddress, phonenumber))
            
    else:
        print("you are not authorised to use this option")    

