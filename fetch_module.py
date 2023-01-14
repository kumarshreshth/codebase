#this module fetch the data from the given sheet as per user need

def fetch_data(position, username_column, password_column, emailaddress_column, phonenumber_column, worksheet):
    list = []
    element_username = str(worksheet.cell(row = position, column = username_column).value)
    element_password = str(worksheet.cell(row = position,column = password_column).value)
    element_emailaddress = str(worksheet.cell(row = position, column = emailaddress_column).value)
    element_phonenumber = str(worksheet.cell(row = position, column = phonenumber_column).value)
    list.extend( [element_username, element_password, element_emailaddress, element_phonenumber])
    dict = {position:list}
    print(dict)
    print("{:10} {:40} {:40} {:40} {:40} ".format('S.NO.','Username','Password','Email Address', 'Phonenumber'))

    for key,value in dict.items():
        username, password, emailaddress, phonenumber = value
        print("{:10} {:40} {:40} {:40} {:40} ".format(str(key), username, password, emailaddress, phonenumber))
