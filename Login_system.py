account_check = False
username_check = False
password_check = False
password_attempt = 0

while account_check == False:
    account = input("Do you have an account; Y/N").upper()
    if account == "Y":
        account_check = True
        login = True
    elif account == "N":
        account_check = True
        create = True

while login == True:
    while username_check == False:
        username = input("Please enter your username; ")
        if username == "jwez04":
            username_check = True
        else:
            print("Invalid username")
    while password_check == False:
        password = input("Please enter your password; ")
        if password == "password":
            password_check = True
            login = False
        else:
            print("Incorrect password please try again you have", 3 - password_attempt, " attempts left.")
            password_attempt = password_attempt + 1
        if password_attempt == 3:
            quit()

dob_check = Faclse:
while create == True:

    name = input("Please enter your name; ")
    dob = input("please enter your Date of Birth; DD/MM/YEAR")
