import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None


def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM employee")
    rows = cur.fetchall()

    for row in rows:
        print(row)

def main():

    database = "/opt/sqlite/company.db"

    # create a database connection
    conn = create_connection(database)
    select = select_all_tasks(conn)
    print(select)

if __name__ == '__main__':

    main()
