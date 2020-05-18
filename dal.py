import sqlite3
from datetime import date
from passwordgenerator import pwgenerator
import bcrypt


def add_password(con,site,user,user_id):
    c = con.cursor()
    
    today = date.today()
    password = pwgenerator.generate()

    sql = """INSERT INTO passwords 
            (site,user,password,date,user_id) VALUES
            (?,?,?,?,?)
          """
    
    c.execute(sql,(site.lower(),user.lower(),password,today,user_id))
    con.commit()
    return password

def get_all_passwords(con,user_id):
    c = con.cursor()

    sql = "SELECT id,site,user,password FROM passwords WHERE user_id=?"
    c.execute(sql,(user_id,))

    result = c.fetchall()
    for row in result:

        print(row)
   
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
