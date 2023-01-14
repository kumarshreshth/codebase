# this module test whether the inputted password is valid or not
def digitValidity(password):
    message = ""
    count = 0
    checklist = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    for c in password:
        if c in checklist:
            count += 1
            break
    if count == 1:
        return message
    else:
        message = "your password does not contain number"
        return message


def charValidity(password):
    message = ""
    capital_letter_count = 0
    small_letter_count = 0
    for pas in password:
        if ord(pas) in range(65, 91):
            capital_letter_count += 1
            break
    for pas in password:
        if ord(pas) in range(97, 122):
            small_letter_count += 1
            break
    if capital_letter_count != 1 and small_letter_count != 1:
        message = "invalid please enter character"
    if capital_letter_count != 1 and small_letter_count == 1:
        message = "please include capital character"
    if capital_letter_count == 1 and small_letter_count != 1:
        message = "please include small character"
    return message


def lengthValidity(password):
    message = ""
    n = len(password)
    if n >= 8 and n<50:
        return message
    if n<8:
        message = "your password is too short it must contain at least 8 character"
        return message
    if n>50:
        message="your password is too long it must be less than 50 character"
        return message


def specialcharValidity(password):
    message = ""
    count = 0
    checklist = ["-","`","~","/","_","!", "@", "#", "$", "%", "^", "&",".","<",">","[","]","{","}","|",":",";","'",'"',"*", "(", ")"]
    for c in password:
        if c in checklist:
            count += 1
            break
    if count == 1:
        return message
    else:
        message = "your password does not contain any special character"
        return message



def checkchar(password):
    message=""
    checklist=["?","+","="," "]
    empty=[]
    temp=[]
    for c in password:
        if c in checklist:
            empty.append(c)
    for p in empty:
        if p not in temp:
            temp.append(p)
    for k in temp:
        if k==" ":
            sub_message="your password contain empty space "+" "
        else:
            sub_message="your password contain "+str(k) +" "
        message=message+sub_message
    return message  
    
    
    
def usernameValid(password,username):
    message=""
    list_password=[]
    list_username=[]
    list_password[0:]=password
    length_of_password=len(list_password)
    list_username[0:]=username
    count=1
    status=True
    if length_of_password==len(list_username):
        while status==True:
            uppercase=str(list_password[0]).upper()
            lowercase=str(list_password[0]).lower()
            if uppercase==list_username[0] or lowercase==list_username[0]:
                if count<length_of_password and list_password[count]==list_username[count]:
                    count+=1
                else:
                    status=False
            else:
                status=False
        if count==length_of_password:
            message="password contain username"
            
    return message






def password_validation(password,username):
    check = []
    digitValid = digitValidity(password)
    charValid = charValidity(password)
    lengthValid = lengthValidity(password)
    specialcharValid = specialcharValidity(password)
    char_not_included=checkchar(password)
    username_valid=usernameValid(password,username)
    check.extend([digitValid, charValid, lengthValid, specialcharValid,char_not_included,username_valid])
    n = len(check)
    count = 0
    for c in range(0, n):
        if check[c] == "":
            count += 1
    if count == n:
        print("password is accepted")
        return True
    else:
        print("password is not accepted because :")
        for c in range(0, n):
            if check[c] != "":
                print(check[c])
        return False