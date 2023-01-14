# This module generate otp and send mail to respect user using ceredentails present in different databse
import random
import smtplib
import errormessage_module as emm


def otp_generator(recevier_email_address, sender_email_address, sender_password):
    otp = random.randint(100000, 1000000)
    status = email_sending(otp, recevier_email_address, sender_email_address, sender_password)
    return str(otp), status


def email_sending(otp, recevier_email_address, sender_email_address, sender_password):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email_address, sender_password)
    message = "your otp is "+ str(otp)+" don't share it with anyone"
    try:
         server.sendmail(sender_email_address, recevier_email_address, message)
         status = True
    except Exception :
        print(emm.error_messages['emailaddress_error'])
        status = False
    server.quit()
    return status


def email_verified(recevier_email_address, sender_email_address, sender_password, username_userinput, password_userinput):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email_address, sender_password)
    message = "Your email is verified successfully\nFollowing are your credentials :-\nUsername :- "+username_userinput+"\nPassword :- "+password_userinput 
    try:
         server.sendmail(sender_email_address, recevier_email_address, message)
         status = True
    except Exception :
        print(emm.error_messages['emailverified_error'])
        status = False
    server.quit()
    if status == True:
        print("A successful verification of email is sent to your email with your credential ")
    



