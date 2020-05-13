import sqlite3
import bcrypt

# def create_connection(db_file):
#     """ create a database connection to the SQLite database
#         specified by the db_file
#     :param db_file: database file
#     :return: Connection object or None
#     """
#     conn = None
#     try:
#         conn = sqlite3.connect(db_file)
#     except Error as e:
#         print(e)

#     return conn


#create db
#todo create a db if not exists
con = sqlite3.connect('database.db')

#make a cursor
c = con.cursor()

users = """CREATE TABLE IF NOT EXISTS users
            ( id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                email TEXT,
                password TEXT)"""

passwords = """CREATE TABLE IF NOT EXISTS passwords
             ( id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                site TEXT,
                user TEXT,
                password TEXT,
                date DATE,
                user_id INTEGER)"""

sql = """INSERT INTO users 
            (username, email, password) VALUES
            (?,?,?)"""

# c.execute(users)
# con.commit()
# c.execute(passwords)
# con.commit()
#c.execute(sql,("pst","superplams@gmail.com",b'$2b$12$3cjpDz8KA6MKz0NcTyDltegAxvMu2AazGISQ/8j3NT/qgMYg0BWJ6'))
#con.commit()
# c.execute(passwords)

#c.execute("""DROP TABLE passwords """)
# c.execute(""" DROP TABLE users""")
#c.execute("SELECT * FROM passwords")


print(con)
