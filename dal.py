import sqlite3
from datetime import date
from passwordgenerator import pwgenerator
import bcrypt
from cryptography.fernet import Fernet
import base64


def create_suite(password, main_pass):
    padded_str = main_pass.ljust(32, '=') 
    key = base64.urlsafe_b64encode(padded_str.encode()) 
    cipher_suite = Fernet(key)
    return cipher_suite

def cipher_pass(password, main_pass):
    cipher_suite = create_suite(password,main_pass)
    ciphered_text = cipher_suite.encrypt(password.encode())
    return ciphered_text

def decipher_pass(password, main_pass):
    cipher_suite = create_suite(password,main_pass)
    unciphered_text = cipher_suite.decrypt(password)
    return unciphered_text

def add_password(con,site,user,user_id,main_pass):
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
    c = con.cursor()

    sql = "SELECT id,site,user,password FROM passwords WHERE user_id=?"
    c.execute(sql,(user_id,))

    result = c.fetchall()
    for row in result:
        password = {"id":row[0],"site":row[1],"user":row[2],"password":decipher_pass(row[3],main_pass).decode()}
        print(password)

def get_all_users(con):
    c = con.cursor()

    sql = "SELECT * FROM users"
    c.execute(sql)

    result = c.fetchall()
    for row in result:
        print(row)

def get_user(con,username):   
    c = con.cursor()

    sql = "SELECT id, username, password FROM users WHERE username=?"
    c.execute(sql, (username,))

    result = c.fetchall()
    for row in result:
        user = {"id":row[0],"username":row[1],"password":row[2]}
        return user
    
def delete_pass(con,id):
    c = con.cursor()

    sql =  "DELETE FROM passwords WHERE id=?"
    c.execute(sql,(id,))
    con.commit() 

def add_user(con,username,email,password):
    c = con.cursor()
    
    sql = "INSERT INTO users (username,email,password) VALUES (?,?,?)"
    hashed = bcrypt.hashpw(password,bcrypt.gensalt())
    c.execute(sql,(username.lower(),email.lower(),hashed))
    con.commit()

def get_site(con,user_id,site):
    c = con.cursor()
    sql = "SELECT site,user,password FROM passwords WHERE site=? AND user_id=?"
    c.execute(sql,(site,user_id))

    result = c.fetchall()
    for row in result:
        return row
