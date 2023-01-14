#this module is used to update previous data
import passwordvalidation_module
import admin_module as am
import errormessage_module as emm
import phonenumber_validation_module as pvm
import maskpass

def update_details(position, password_column, emailaddress_column, phonenumber_column, worksheet,username, old_password):
    
    new_password = maskpass.askpass(prompt ="enter your password\n", mask = "#")
    if old_password == new_password:
        print("your previous password is same as new password entered, so password is not updated")
    else:
        status_password = passwordvalidation_module.password_validation(new_password,username)
        if status_password == True:
            while True:
                retype_password = input("please confirm your password\n")
                if retype_password == new_password:
                    element_update_password = worksheet.cell(row = position, column = password_column)
                    element_update_password.value = new_password
                    print("your password is updated successfully\n")
                    break
                else:
                    print("confirm password doesnot matched your new password, please try again!")
                    continue
        else:
            print("you password is not updated it will remain same")
   

   
    new_email_address = input("enter your email address\n")
    email_status = am.main(new_email_address, username, new_password)
    if email_status == True :
        element_update_emailaddress = worksheet.cell(row = position, column = emailaddress_column)
        element_update_emailaddress.value = new_email_address
        print("your email address is updated successfully\n")
   
    else:
        print("your email address is not updated it will same")

   
    try : 
        new_phonenumber = int(input("enter your phone number \n"))
        if len(str(new_phonenumber)) == 10:
            try :
                otp_generated = pvm.otp_verifier.otp_sending(new_phonenumber)
                otp_input = input("enter the otp obtained on your phonenumber\t")
                if otp_input == otp_generated :
                    element_update_phonenumber = worksheet.cell(row = position, column = phonenumber_column)
                    element_update_phonenumber.value = "+91-"+str(new_phonenumber)
                    print("the phone number entered is accepted and updated")
                else :
                    print("the entered otp is wrong so the entered phonenumber is not updated")
            except Exception :
                print(emm.error_messages['phonenumber_validation'])
        else :
            print(emm.error_messages['phonenumber_length'])

    except Exception:
        print(emm.error_messages['phonenumber'])