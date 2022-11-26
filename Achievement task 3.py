''' Program asking the user to enter the username and password
Autor: Parth Patel
Date created : 26th November, 2022
Last modified : 26th November, 2022 '''


Username = str(input("Enter your username: "))#asks the user to enter name
password = str(input("Enter password that include 1 uppercase alphabate and atleast 1 number: ")) 

if len(Username) <= 1: #adds the condition, that the name must be greater than one alphbet
    print("Sorry, username must be longer than one letter.") #if the condition results true tan the follwing message gets prints

elif len(Username) >= 21: #adds the condition, that the name must be shorter than twenty one alphbet
    print("Sorry, username cannot be more than 20 letters in length.") #if the condition results true tan the follwing message gets print

elif len(Username) >= 21 and Username <=1: #if thecondition gets true tahn the code asks for the password
    

 if password.islower() and "0,1,2,3,4,5,6,7,8,9" not in password: #condition is created that the password must contain uppercase character and one digit
        print("you must include 1 Uppercase letter and number") #if the above condition is false than the message gets print
        password = input("please try again: ") #asks the user to re-enter the password

