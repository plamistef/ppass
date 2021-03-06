import sqlite3
from datetime import date
from passwordgenerator import pwgenerator
import bcrypt
from cryptography.fernet import Fernet
import base64


def create_suite(password, main_pass):
    """ Takes the user's main password and the current generated password
    and generates a cipher_suite for encoding and decoding.

    :param: password, main_pass 
    the generated password for the selected site, the users main password
    :return: cipher_suite object
"""
    padded_str = main_pass.ljust(32, '=') 
    key = base64.urlsafe_b64encode(padded_str.encode()) 
    cipher_suite = Fernet(key)
    return cipher_suite


def cipher_pass(password, main_pass):
    """  Cipher's the passed password.
    :param: password, main_pass
    the generated password for the selected site, the users main password
    :return: the encrypted password
"""
    cipher_suite = create_suite(password,main_pass)
    ciphered_text = cipher_suite.encrypt(password.encode())
    return ciphered_text


def decipher_pass(password, main_pass):
    """ Decipher's the passed password.
    :param: password, main_pass 
    the generated password for the selected site, the users main password
    :return: the decrypted password
"""
    cipher_suite = create_suite(password,main_pass)
    unciphered_text = cipher_suite.decrypt(password)
    return unciphered_text


def add_password(con,site,user,user_id,main_pass):
    """ Adds a new password to the database
    :param: con,site,user,user_id,main_pass 
    db connection, website, username, the logged in user, their password 
    :return: the auto generated secure password 
"""
    c = con.cursor()
    
    today = date.today()

    password = pwgenerator.generate()
    ciphered_pass = cipher_pass(password, main_pass)

    sql = """INSERT INTO passwords 
            (site,user,password,date,user_id) VALUES
            (?,?,?,?,?)
            """
    c.execute(sql,(site.lower(),user.lower(),ciphered_pass,today,user_id))
    con.commit()
    return password



def get_all_passwords(con,user_id,main_pass):
    """ Fetches all password for the current user
    :param con,user_id,main_pass: db connection, logged in user's id and their pass
    :return: None
"""
    c = con.cursor()

    sql = "SELECT id,site,user,password FROM passwords WHERE user_id=?"
    c.execute(sql,(user_id,))

    result = c.fetchall()
    for row in result:
        password = {"id":row[0],"site":row[1],"user":row[2],"password":decipher_pass(row[3],main_pass).decode()}
        print(password)


def get_all_users(con):
    """ Fetches all entries from the user's table
    :param con: db connection
    :return: None
"""
    c = con.cursor()

    sql = "SELECT * FROM users"
    c.execute(sql)

    result = c.fetchall()
    for row in result:
        print(row)


def get_user(con,username):   
    """ Fetches the user with the passed username from the users table.
    :param con, username: db connection, the username we are looking for
    :return: user dictionary object or None
"""
    c = con.cursor()

    sql = "SELECT id, username, password FROM users WHERE username=?"
    c.execute(sql, (username,))

    result = c.fetchall()
    for row in result:
        user = {"id":row[0],"username":row[1],"password":row[2]}
        return user
    

def delete_pass(con,id):
    """ Deletes a password by selected id
    :param con, id: db connection, the id of the password
    :return: None
"""
    c = con.cursor()

    sql =  "DELETE FROM passwords WHERE id=?"
    c.execute(sql,(id,))
    con.commit() 


def add_user(con,username,email,password):
    """ Adds a user to the users table.
    :param con,username,email,password: db connection, username, email, password
    :return: None
"""
    c = con.cursor()
    
    sql = "INSERT INTO users (username,email,password) VALUES (?,?,?)"
    hashed = bcrypt.hashpw(password,bcrypt.gensalt())
    c.execute(sql,(username.lower(),email.lower(),hashed))
    con.commit()


def get_site(con,user_id,site):
    """ Fetches the website for the particular user which respond to the passed site name
    :param con,user_id,site: db connection, the user id, website name
    :return: the website or None
"""
    c = con.cursor()
    sql = "SELECT site,user,password FROM passwords WHERE site=? AND user_id=?"
    c.execute(sql,(site,user_id))

    result = c.fetchall()
    for row in result:
        return row
