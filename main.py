import sqlite3
import os,sys
import bcrypt,getpass
import setup,dal,menu

sys.path.append(os.path.realpath("."))

import inquirer
from inquirer import errors

"""
    Creates a database connection if it does not exist 
"""
database = "./database.db"
con = setup.create_connection(database)

"""
    Checks if the user has an account, if not it promts them to create one
"""
login = inquirer.confirm(message= "Do you have an account", default=True)

if (login):
    pass
else:
    username = inquirer.text(message="Enter your username")
    foundUsername = dal.get_user(con,username)
    if(foundUsername != None):
        print("The username is already taken")
    else:
        email = inquirer.text( message="Enter your email")
        pwd = getpass.getpass()
        dal.add_user(con,username,email,pwd.encode())

"""
    Login into user's account and display the internal menu
"""
print("Login")
username = inquirer.text(message="Enter your username")
foundUser = dal.get_user(con,username)
password = getpass.getpass()

try: 
    if(foundUser['username'] == username):
        
        #turn password string into a byte string
        if (bcrypt.checkpw(password.encode(), foundUser['password'])):
            os.system('clear')
            print("Welcome ladies and gents")
            menu.menu(con,foundUser,password)
        else:
            print("try harder")
except:
    print("sorry try again")
    



