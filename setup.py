import sqlite3

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


# #create db
# #todo create a db if not exists
# con = sqlite3.connect('database.db')
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        create_tables(conn)
    except sqlite3.Error as e:
        print(e)

    return conn


def create_tables(conn):
    #database = r"/Users/pst/Desktop/py-env/ppass/database.db"
   # con = create_connection(database)
    cursor = conn.cursor()    

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

    cursor.execute(users)
    cursor.execute(passwords)
    conn.commit()

# sql = """INSERT INTO users 
#             (username, email, password) VALUES
#             (?,?,?)"""

# c.execute(users)
# con.commit()
# c.execute(passwords)
# con.commit()
#con.commit()
# c.execute(passwords)

#c.execute("""DROP TABLE passwords """)
# c.execute(""" DROP TABLE users""")
#c.execute("SELECT * FROM passwords")