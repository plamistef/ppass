import sqlite3
import os
import new_password
import bcrypt

# ADMIN_PASSWORD = "admin"

# os.system('clear')
con = sqlite3.connect('database.db')

#new_password.get_user(con,"pst")
#user = new_password.get_user(con,"pst")
#print(user)

##fix this
username = input("Enter your username: \n")
password = input("Enter your pass: \n")

foundUser = new_password.get_user(con,username)
foundUser_id = foundUser[0]
foundUser_username = foundUser[1]
foundUser_password = foundUser[2]

if (foundUser_username == username):
    #turn password string into a byte string
    if (bcrypt.checkpw(password.encode(), foundUser_password)):
        os.system('clear')
        while(True):
            #os.system('clear')
            print("Welcome ladies and gents")
            print("Commands: ")
            print("a = see all passwords")
            print("n = add new password")
            print("d = delete password")
            print("q = quit")

            userInput = input("Enter command: ")
            if userInput == 'a':
                new_password.view_all(con,foundUser_id)
            elif userInput == 'n':
                site = input("Enter website: \n")
                user = input("Enter username/email: \n")
                new = new_password.add_password(con,site,user,foundUser_id)
                print(new)
            elif userInput == 'd':
                pass
            elif userInput == 'q':
                break