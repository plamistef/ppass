import sqlite3

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

""" creates the tables in the SQLite database
        specified by the connection
    :param conn: connection
    :return: None
    """
def create_tables(conn):

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

