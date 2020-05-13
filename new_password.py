import sqlite3
from datetime import date
from passwordgenerator import pwgenerator


#todo hash the pass
def create(con,site,user):
    c = con.cursor()
    
    today = date.today()
    password = pwgenerator.generate()

    sql = """INSERT INTO passwords 
            (site,user,password,date) VALUES
            (?,?,?,?)
          """
    
    c.execute(sql,(site,user,password,today))
    return password

def view_all(con):
    c = con.cursor()

    sql = "SELECT * FROM passwords"
    c.execute(sql)

    result = c.fetchall()
    for row in result:
        print(row)
   
def view_all_users(con):
    c = con.cursor()

    sql = "SELECT * FROM users"
    c.execute(sql)

    result = c.fetchall()
    for row in result:
        print(row)

def get_user(con,username):   
    c = con.cursor()

    c.execute("SELECT username, password FROM users WHERE username=?", (username,))

    #sql = "SELECT * FROM users WHERE username=%s"
    #c.execute(sql,(username))
    result = c.fetchall()
    for row in result:
        #print(row)
        return row


