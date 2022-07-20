#!/usr/bin/env python3

# Module 1 Assignment - COMP 662 - Programming Databases with Python - 04/12/2021 to 06/10/2021
# Author: Scott Schmidl

import sqlite3

def connect_db(database):

    '''
    RETURN: CONNECT TO DATABASE
    ARGUMENT: DATEBASE - STRING
    '''

    return sqlite3.connect(database)

def exec_query(query, cursor):

    '''
    RETURNS: AN EXECUTED QUERY
    ARGUMENTS: QUERY - STRING
                CURSOR - OBJECT
    '''

    cursor.execute(query)

    return cursor.fetchall()


def main():

    # DEFINES DATABASE, MAKES CONNECTION, AND GETS CURSOR OBJECT
    database = 'chinook.db'
    con = connect_db(database)
    cur = con.cursor()

    # SET QUERY, EXECUTE, AND FETCH
    query = '''SELECT * FROM artists'''
    artists = exec_query(query, cur)

    # PRINT OUT THE ARTISTS NAMES
    print('Here are the artist names from the Artist table:\n')
    for artist in artists:
        print(artist[1])

    # CLOSE THE CONNECTION
    if con:
        con.close()

    print('\nThat\'s all folks. See You Soon!')

if __name__ == '__main__':
    main()