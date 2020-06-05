import dal,sys,os
sys.path.append(os.path.realpath("."))

import inquirer
from inquirer import errors



def menu(con,foundUser,password):
    """ The internal menu after the user logs in.
    The user can choose to see, add or delete passwords.
    :param con, foundUser, password: db connection, the logged in user, their password
    :return: None
"""
    q = [
            inquirer.List('commands',
                message='What are you interested in?',
                choices=['see all passwords', 'add a new password','delete a password','quit'],
                )]
    while(True):
            print("\n")
            a = inquirer.prompt(q)
            if a['commands'] == 'see all passwords':
                dal.get_all_passwords(con,foundUser['id'],password)
            elif a['commands'] == 'add a new password':
                site = inquirer.text(message="Enter the name of the website")
                foundSite = dal.get_site(con,foundUser['id'],site)
                if(foundSite != None):
                    print("You have already created a password for this website")                        
                else:  
                    user = inquirer.text(message="Enter username/email")
                    new = dal.add_password(con,site,user,foundUser['id'],password)
                    print("\n",new)
            elif a['commands'] == 'delete a password':
                dal.get_all_passwords(con,foundUser['id'],password)
                to_delete = inquirer.text(message="Enter password id")
                dal.delete_pass(con,to_delete)
            elif a['commands'] == 'quit':
                break