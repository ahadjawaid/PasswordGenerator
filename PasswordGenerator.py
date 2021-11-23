import random
import pyperclip
import string

def generator(type, numCharcters):
    #makes a string consiting of letters, number, and special charcters
    specialCharacters = string.ascii_letters + string.digits + string.punctuation
    #makes a string with letters and digits
    noSpecialCharacters = string.ascii_letters + string.digits
    #creates an empty variable to store password
    password = ""
    print(type)
    #if the type wants special charcters it uses the specialCharcters string
    if type in "yY":
        for _ in range(numCharcters):
            #adds random characters from the special charcters list to the password string
            password += specialCharacters[random.randrange(0, len(specialCharacters))]
    #uses non-special charcter string
    elif type in "nN":
        for _ in range(numCharcters):
            #adds random characters from the non special charcters list to the password string
            password += noSpecialCharacters[random.randrange(0, len(noSpecialCharacters))]
    else:
        #handles error if they inputed wrong input
        print("Please enter 'y' or 'n'")
    #copies password to clip board and returns password
    pyperclip.copy(password)
    return password

dictType = str(input("Please input (y or n) for special charcter or no special charcters\n"))
numberCharacters = int(input("Please input the amount of characters\n"))
print(generator(dictType, numberCharacters))