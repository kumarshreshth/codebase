# This module send otp for phone verification to the user phone number

from twilio.rest import Client
import random


class otp_verifier:
    def otp_sending(phonenumber):
        otp = str(random.randint(100000, 1000000))
        try:
            client = Client("AC2d105eb794c565cc7e08fd6cb6efa39b", "5f24a500ac4b5f96aa1b7d8af5231e45")
            client.messages.create( to ="+91-"+str(phonenumber), from_= "+16692022569", body = "Your otp is "+ otp+" don't share with anyone")
        except  Exception:
            print("this is trial server cant send message to any number kindly add this number to admin's twilio account")
        return otp





