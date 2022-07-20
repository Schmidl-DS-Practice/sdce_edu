#!/usr/bin/env python3

# Module 7 Assignment - COMP 662 - Programming Databases with Python - 04/12/2021 to 06/10/2021
# Author: Scott Schmidl

from sqlite3.dbapi2 import Error
from ClassSQLite import EsQuLite as eql
import logging

filename = "roster.db"
db_title = "roster"
to_perform = eql(filename, db_title)
con = to_perform.db_connect()
cur = to_perform.db_cursor(con)

def view():
    """VIEW QUERY RECORD(S)

    Args:
        to_view (CLASS): USED FOR CON/CUR
        cur (CLASS): CURSOR TO USE FOR QUERY
        query (STRING): QUERY TO VIEW

    Returns:
        LIST: THE RESULTING QUERY
    """

    view_query = """
        SELECT *
        FROM students"""

    try:
        return to_perform.db_runquery(cur, view_query)
    except Error as e:
        logging.error(f"Query incorrect. Try again...\n\n{e}")

def insert(nm, addr, city, id):
    """UPDATE TABLE

    Args:
        to_insert (CLASS): USED FOR CON/CUR
        cur (CLASS): CURSOR TO USE FOR UPDATE
        query (STRING): QUERY TO UPDATE
    """

    insert_query = f"""
        INSERT INTO students (name, addr, city, id)
        VALUES ('{nm}', '{addr}', '{city}', '{id}')"""

    try:
        to_perform.db_runquery(cur, insert_query)
        logging.info("Table successfully updated")
        con.commit()
    except Error as e:
        logging.error(f"Table not updated\n\n{e}")

def searching(nm, addr, city):
    """SEARCH FOR A RECORD(S)

	Args:
		to_search (CLASS): USED FOR CON/CUR
		cur (CLASS): CURSOR TO USE FOR SEARCH
		query (STRING): QUERY TO SEARCH

	Returns:
        LIST: RECORD(S) FOR WHICH TO SEARCH
	"""

    search_query = f"""
            SELECT name, addr, city, id
            FROM students
            WHERE name = '{nm}' AND
                addr = '{addr}' AND
                city = '{city}';"""

    try:
        return to_perform.db_runquery(cur, search_query)

    except Error as e:
        logging.error(f"Record not found\n\n{e}")

def delete(nm):
    """DELETE RECORD(S)

    Args:
        to_delete (CLASS): USED FOR CON/CUR
        cur (CLASS): CURSOR TO USE FOR DELET
        query (STRING): QUERY TO DELETE

    Returns:
        CLASS: LOGGING INFO FOR SUCCESSFUL DELETE
    """

    delete_query = f"""
            DELETE FROM students WHERE name = '{nm}'"""

    try:
        to_perform.db_runquery(cur, delete_query)
        logging.info("Record(s) successfully deleted")
        con.commit()
    except Error as e:
        logging.error(f"Record(s) does not exist:\n\n{e}")

def main():

    # DEFINE VARIABLES/CONNECT TO DATABASE/SET CURSOR
    filename = "roster.db"
    db_title = "roster"
    to_perform = eql(filename, db_title)
    con = to_perform.db_connect()
    cur = to_perform.db_cursor(con)

    # QUERY TO BE VIEWED
    view_query = """
        SELECT *
        FROM students"""
    view_result = view(to_perform, cur, view_query)
    print(f"\n{view_result}")

    # INSERT INTO TABLE
    nm = input('Enter name: ')
    addr = input('Enter address: ')
    city = input('Enter city: ')
    id = input('Enter id: ')
    insert_query = f"""
        INSERT INTO students (name, addr, city, id)
        VALUES ('{nm}', '{addr}', '{city}',  '{id}')"""
    #insert(to_perform, cur, con, insert_query)

    # RECORD FOR WHICH TO SEARCH
    search_query = """
        SELECT name
        FROM students
        WHERE name = 'Liam'"""
    # search_result = searching(to_perform, cur, search_query)
    # print(f"\n{search_result}")

    # RECORD TO DELETE
    nm = input('Enter name: ')
    delelte_query = f"""
            DELETE FROM students WHERE name = '{nm}'"""
    #delete(to_perform, cur, con, delete_query)

    # IF THE CONNECTION IS OPEN CLOSE IT
    to_perform.db_close()

    print('Thanks for checking out the database. Bye!')

if __name__ == "__main__":
    main()