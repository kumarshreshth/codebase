import openpyxl as op
def digitValidity(password):
    m=""
    count=0
    checklist=["1","2","3","4","5","6","7","8","9","0"]
    for c in password:
        if c in checklist:
            count+=1
            break
    if count==1:
        return m
    else:
        m="your password does not contain number"
        return m


def charValidity(password):
    m=""
    c=0
    d=0
    for pas in password:
        if ord(pas)  in range(65,91):
            c+=1
            break
    for pas in password:
        if ord(pas) in range (97,122):
            d+=1
            break
    if c!=1 and d!=1:
        s="invalid please enter character"
        m=m+s
    if c!=1 and d==1:
        s="please include capital character"
        m=m+s
    if c==1 and d!=1:
        s="please include small character"
        m=m+s
    return m
        


def lengthValidity(password):
    m=""
    n=len(password)
    if n >=8:
        return m
    else:
        m="your password is too short it must contain at least 8 character"
        return m
    

def specialcharValidity(password):
    m=""
    count =0
    checklist=["!","@","#","$","%","^","&","*","(",")"]
    for c in password:
        if c in checklist:
            count+=1
            break
    if count==1:
        return m
    else:
        m="your password doesnot contain any special character"
        return m
    
        
            
def passwordvalid(password):
    check=[]
    digitValid=digitValidity(password)
    charValid=charValidity(password)
    lengthValid=lengthValidity(password)
    specialcharValid=specialcharValidity(password)
    check.extend([digitValid,charValid,lengthValid,specialcharValid])
    n=len(check)
    count=0
    for c in range(0,n):
        if check[c]=="":
            count+=1
    if count==n:
        print("password is accepted")
        return True
    else:
        print("password is not accepted due ")
        for c in range (0,n):
            if check[c]!="":
                print(check[c])
        return False
                
                
def specialValidity(email_address):
    m=""
    count=0
    checklist=["@"]
    for c in email_address:
        if c in checklist:
            count+=1
            break
    if count!=1:
        m="your email address doesnot contain @"
    return m   

def emailValidity(email_address):
    check=[]
    specialchar=specialValidity(email_address)
    check.extend([specialchar])
    n=len(check)
    count=0
    for c in range(0,n):
        if check[c]=="":
            count+=1
    if count==n:
        print("email address accepted")
        return True
    else:
        print("email address is not accepted due to")
        for c in range(0,n):
            if check[c]!="":
                print(check[c])
        return False
            
wb=op.load_workbook('test.xlsx')
wb.active
sheet=input("enter usertype:\n")
ws=wb[sheet]
if sheet=="local" or sheet=="global":
    for c in range(1,ws.max_column+1):
        element=ws.cell(row=1,column=c)
        if element.value=="PASSWORD":
            k=c
            break
    for c in range(1,ws.max_column+1):
        element=ws.cell(row=1,column=c)
        if element.value=="USERNAME":
            q=c
            break
    for c in range(1,ws.max_column+1):
        element=ws.cell(row=1,column=c)
        if element.value=="EMAIL ADDRESS":
            r=c
            break
        
        
        
    username=input("enter your username\n")
    password=""
    count=0
    row1=ws.max_row
    for c in range (1,row1+1):
        val=ws.cell(row=c,column=q)
        if username==val.value:
            count+=1
            print("\nit already exist in "+sheet+" sheet")
            print("if you want to update your details enter 1 else enter 2 to exit")
            choice_password=input()
            if choice_password=="2":
                break
            if choice_password=="1":
                password=input("enter your password\n")
                m=passwordvalid(password)
                element_update_password=ws.cell(row=c,column=k)
                if m==True:
                    element_update_password.value=password
                email_address=input("enter your email address\n")
                j=emailValidity(email_address)
                element_update_emailaddress=ws.cell(row=c,column=r)
                if j==True:
                  element_update_emailaddress.value=email_address
            else:
                print("inputted value is wrong")
            break
    if count!=1:
        password=input("enter your password\n")
        m=passwordvalid(password)
        if m==True:
            element_username=ws.cell(row=row1+1,column=q)
            element_username.value=username
            element_password=ws.cell(row=row1+1,column=k)
            element_password.value=password
            email_address=input("enter your email address\n")
            j=emailValidity(email_address)
            element_emailaddress=ws.cell(row=row1+1,column=r)
            if j==True:
                element_emailaddress.value=email_address
    
    wb.save("test.xlsx")
else:
    print("please enter valid datatype")
