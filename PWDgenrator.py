import random

#The Characters that you can use 
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!£$%^&*(`)"

#The main loop
while 1:
    #Inputs
    password_len = int(input("What length would you like your password to be : "))
    password_count = int(input("How many passwords would you like : "))
    #Main genrating process
    for x in range(0,password_count):
        password  = ""
        for x in range(0,password_len):
            password_char = random.choice(chars)
            password  = password + password_char
        with open("PWD.txt", "w") as file:
            file.write(password)