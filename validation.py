import re
password = input("Password: ")

def checkLetterLower (num) :
    global password
    status = any(char.islower() for char in password)
    if status :
        return status
    else :
        if num == 0 :
            print("At least 1 letter between [a-z]")
            return status
        else :
            return status

def checkLetterUpper (num) :
    global password
    status = any(char.isupper() for char in password)
    if status :
        return status
    else :
        if num == 0 :
            print("At least 1 letter between [A-Z]")
            return status
        else :
            return status

def checkNumber (num) :
    global password
    status = bool(re.search(r'[0-9]', password)) 

    if status :
        return status
    else :
        if num == 0 :
            print("At least 1 number between [0-9]")
            return status
        else :
            return status

def checkChar (num) :
    global password
    status = bool(re.search(r'[$,#,@]', password)) 

    if status :
        return status
    else :
        if num == 0 :
            print("At least 1 character from [$#@]")
            return status
        else :
            return status

def minLen (num) :
    global password
    status = False

    if len(password) >= 6 :
        status = True
        return status
    else :
        status = False
        if num == 0 :
            print("Minimum length 6 characters")
            return status
        else :
            return status

def maxLen (num) :
    global password
    status = False

    if len(password) <= 16 :
        status = True
        return status
    else :
        status = False
        if num == 0 :
            print("Maximum length 16 characters")
            return status
        else :
            return status
    
def Validate () :
    if checkLetterLower(1) and checkLetterUpper(1) and checkNumber(1) and checkChar(1) and minLen(1) and maxLen(1) :
        return "\nPassword is in correct form"
    else :
        return "\nPassword is not in correct form"

checkLetterLower(0)
checkLetterUpper(0)
checkNumber(0)
checkChar(0)
minLen(0)
maxLen(0)
print(Validate())

