#Name: Dylan Avritt
#Class: 5th Hour
#Assignment: HW10

#1. Print Hello World!
print("Hello World!")
#2. Create three different boolean variables named wifi, login, and admin.
wifi = True
Login = True
Admin = True

#3. Create a separate integer variable that denotes the number of times
#someone with admin credentials has logged in.
admins_Logged_in = 1
#4. Create a nested if statement that checks to see if wifi is true,
#login is true, and admin is true. If they are all true, print a
#welcome message and increase the integer variable by one. If one of them
#is false, print an error message telling them which one they are "missing".

if wifi == True:
    if Login == True:
        if Admin == True:
            print("Welcome Admin!")
            admins_Logged_in += 1
            print(admins_Logged_in, "Admins logged in")
        else:
            print("You are not an Admin")
    else:
        print("Wrong login, Try again")
else:
    print("Wrong Wifi or wifi error")
