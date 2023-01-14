#this module allows the entry of new user
import passwordvalidation_module
import admin_module as am
import errormessage_module as emm
import phonenumber_validation_module as pvm
import serialnumber_module
import maskpass


def newuser(username, username_column, password_column, emailaddress_column, phonenumber_column, worksheet, serialnumber_column):
    rowmax = worksheet.max_row
    password = maskpass.askpass(prompt = "enter your password\n", mask = "#")
    status_password = passwordvalidation_module.password_validation(password,username)
    if status_password == True:
        serialnumber_module.serialnumber_newuser(serialnumber_column, worksheet)
        element_username = worksheet.cell(row = rowmax + 1, column = username_column)
        element_username.value = username
        element_password = worksheet.cell(row = rowmax + 1, column = password_column)
        element_password.value = password
        print("new user is added to database\n")
        email_address = input("enter your email address\n")
        email_status = am.main(email_address,username,password)
        if email_status == True :
            element_emailaddress = worksheet.cell(row = rowmax + 1, column = emailaddress_column)
            element_emailaddress.value = email_address
            print("the entered email address is accepted")
        else:
            print("the entered email address is not accepted ")
        try:
            phonenumber = int(input("enter your phone number \n"))
            if len(str(phonenumber)) == 10:
                try :
                    otp_generated = pvm.otp_verifier.otp_sending(phonenumber)
                    otp_input = input("enter the obtained OTP on your phone number\t")
                    if otp_input == otp_generated :
                        element_phonenumber = worksheet.cell(row = rowmax +1, column = phonenumber_column)
                        element_phonenumber.value = "+91-"+str(phonenumber)
                        print("the entered number is accepted")
                    else :
                        print("enter otp is wrong")
                except Exception as e:
                    print(str(e))
  
            else :
                print(emm.error_messages['phonenumber_length'])
        
        except Exception :
            print(emm.error_messages['phonenumber'])
