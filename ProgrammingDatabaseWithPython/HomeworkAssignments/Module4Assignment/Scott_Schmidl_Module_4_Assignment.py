#!/usr/bin/env python3

# Module 4 Assignment - COMP 662 - Programming Databases with Python - 04/12/2021 to 06/10/2021
# Author: Scott Schmidl

import sqlite3
import logging

logging.basicConfig(level=logging.DEBUG,format="[dbmovies]: %(asctime)s: %(levelname)s: %(message)s")

def connect_db(database):

    '''
    RETURN: CONNECT TO DATABASE
    ARGUMENT: DATEBASE - STRING
    '''

    return sqlite3.connect(database)

def exec_query(query, cur):

    '''
    RETURNS: AN EXECUTED QUERY
    ARGUMENTS: QUERY - STRING
                CURSOR - OBJECT
    '''
    try:
        cur.execute(query)
    except:
        logging.error('Query Not Successful...')
    return cur.fetchall()

def update_db(query, cur, con):

    '''
    RETURNS: NONE
    ARGUMENTS: QUERY - STRING
                CUR - CURSOR OBJECT
                CON - CONNECTION OBJECT
    FUNCTIONS UPDATES THE REQUESTED RECORD
    '''

    updated_record = exec_query(query, cur)
    if len(updated_record) == 0:
        logging.error('Already updated. Moving on...')
    else:
        logging.debug('Record Updated...')
        con.commit()

def delete_record(query, cur, con):

    '''
    RETURNS: NONE
    ARGUMENTS: QUERY - STRING
                CUR - CURSOR OBJECT
                CON - CONNECTION OBJECT
    FUNCTIONS DELETES THE REQUESTED RECORD
    '''

    deleted_record = exec_query(query, cur)
    if len(deleted_record) == 0:
        logging.error('Record does not exist. Moving on...')
    else:
        logging.debug('Record Deleted...')
        con.commit()

def lookup_year(cur):

    """
    RETURNS: NONE
    ARUGMENTS: CUR - CURSOR OBJECT
    FUNCTIONS DISPLAYS THE REQUESTED QUERY BY YEAR
    """

    while True:
        year = input('\nPlease enter a year to lookup: ')
        lookup_query = f"""
                        SELECT Movie.name AS Title, Movie.year AS Year, Movie.minutes AS Length, Category.name AS Genre
                        FROM Movie
                        JOIN Category
                        ON Movie.categoryID = Category.categoryID
                        WHERE year = {year}
                        """

        # GET MOVIE INFO
        movie_data = exec_query(lookup_query, cur)
        if len(movie_data) > 0:
            # GET HEADERS
            col_names = get_headers(lookup_query, cur)
            print(f'{col_names[0]}\t\t{col_names[1]}\t{col_names[2]}\t{col_names[3]}')
            for movie in movie_data:
                print(f'{movie[0]}\t{movie[1]}\t{movie[2]}\t{movie[3]}')
        else:
            logging.error(f'Sorry, no movie in our database for {year}.')

        another_year = input('\nLook up another year (y/n)? ').lower()

        if another_year != 'y' :
            break

def get_headers(query, cur):

    '''
    RETURNS: LIST OF COLUMN NAMES
    ARGUMENTS: QUERY - STRING
                CUR - CURSOR OBJECT
    PRINTS THE HEADERS OF REQUESTED QUERY
    '''

    cur.execute(query)
    return list(map(lambda x: x[0], cur.description))

def main():

    print('Welcome to the Movie DB!\n')

    # DEFINES DATABASE, MAKES CONNECTION, AND GETS CURSOR OBJECT
    database = 'dbmovies.sqlite'
    con = connect_db(database)
    logging.debug(f'Connected to {database}...')
    cur = con.cursor()

    # UPDATE DATABASE
    update_query = """
    UPDATE Movie SET year = '1995' WHERE name = 'Toy Story'
    """
    update_db(update_query, cur, con)

    # DELETE RECORD
    delete_query = """
    DELETE FROM Movie WHERE name = 'Lawrence of Arabia'
    """
    delete_record(delete_query, cur, con)

    # LOOKUP MOVIE BY YEAR
    lookup_year(cur)

    # CLOSE THE CONNECTION
    if con:
        con.close()
        print()
        logging.debug(f'{database} has been closed...')

    print('Bye for now - see you at the movies!')

if __name__ == '__main__':
    main()
