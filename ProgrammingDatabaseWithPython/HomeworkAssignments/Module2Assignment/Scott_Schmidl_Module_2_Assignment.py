#!/usr/bin/env python3

# Module 2 Assignment - COMP 662 - Programming Databases with Python - 04/12/2021 to 06/10/2021
# Author: Scott Schmidl

import sqlite3

def db_connect(database):

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
    database = 'movies_test.db'
    con = db_connect(database)
    cur = con.cursor()

    # SET QUERY, EXECUTE, AND FETCH
    query1 = '''SELECT * FROM movies_info_1'''
    # query2 = '''SELECT * FROM movies_info_2'''
    movie_data1 = exec_query(query1, cur)
    # movie_data2 = exec_query(query2, cur)

    # PRINT OUT THE GENRE, TITLE, DIRECTOR
    print('Here is some movie data from the movies_info_1 table:\n')
    for _, g, t, dir, in movie_data1:
        print(f'Genre: {g}')
        print(f'Title: {t}')
        print(f'Director: {dir}\n')

    # CLOSE THE CONNECTION
    if con:
        con.close()

    print('That\'s all folks. See You Soon!')

if __name__ == '__main__':
    main()
