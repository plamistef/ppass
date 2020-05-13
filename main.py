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
#while (True):
foundUser = new_password.get_user(con,username)
if (foundUser[0] == username):
    #turn password string into a byte string
    if (bcrypt.checkpw(password.encode(), foundUser[1])):
        print("fuck yes")

# while username == new_password.get_user(con,username):
#     os.system('clear')
#     print("")
#     #connect = input("Wrong password, please try again: \n")
#     if connect == 'q' : break


# new_password.view_all_users(con)
# new_password.view_all(con)

# while(True):
#     #os.system('clear')
#     print("Welcome ladies and gents")
#     print("Commands: ")
#     print("a = see all passwords")
#     print("n = add new password")
#     print("d = delete password")
#     print("q = quit")

#     userInput = input("Enter command: ")
#     if userInput == 'a':
#         new_password.view_all(con)
#     elif userInput == 'n':
#         site = input("Enter website: \n")
#         user = input("Enter username/email: \n")
#         new = new_password.create(con,site,user)
#         print(new)
#     elif userInput == 'd':
#         pass
#     elif userInput == 'q':
#         break