import sqlite3
import os,sys,re
import bcrypt,getpass
import setup,dal

sys.path.append(os.path.realpath("."))

import inquirer
from inquirer import errors

database = r"/Users/pst/Desktop/py-env/ppass/database.db"
con = setup.create_connection(database)

login = inquirer.confirm(message= "Do you have an account", default=True)

if (login):
    pass
else:
    username = inquirer.text(message="Enter your username")
    #todo email validation
    email = inquirer.text( message="Enter your email")
    parola = getpass.getpass()

    dal.add_user(con,username,email,parola.encode())


username = inquirer.text(message="Enter your username")
password = getpass.getpass()

foundUser = dal.get_user(con,username)

if (foundUser['username'] == username):
    #turn password string into a byte string
    if (bcrypt.checkpw(password.encode(), foundUser['password'])):
        os.system('clear')
        print("Welcome ladies and gents")
        q = [
            inquirer.List('commands',
                  message='What are you interested in?',
                  choices=['see all passwords', 'add new password','quit'],
                  )]

        while(True):
            print("\n")
            a = inquirer.prompt(q)
            if a['commands'] == 'see all passwords':
                dal.get_all_passwords(con,foundUser['id'])
            elif a['commands'] == 'add new password':
                site = inquirer.text(message="Enter the name of the website")
                foundSite = dal.get_site(con,foundUser['id'],site)
                print(foundSite)
                # user = inquirer.text(message="Enter username/email")
                # new = dal.add_password(con,site,user,foundUser['id'])
                # print("\n",new)
            # elif a['commands'] == 'delete password':
            #     to_delete = input("Enter password id: \n")
            #     dal.delete_pass(con,to_delete)
            elif a['commands'] == 'quit':
                break
    