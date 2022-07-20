#!/usr/bin/env python3

# Module 3 Assignment - COMP 662 - Programming Databases with Python - 04/12/2021 to 06/10/2021
# Author: Scott Schmidl

import sqlite3
import logging

logging.basicConfig(level=logging.DEBUG,format="[Movies]: %(asctime)s: %(levelname)s: %(message)s")

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

    cur.execute(query)
    return cur.fetchall()

def create_table(tables, cur):

    '''
    CREATES TABLES
    ARGUMENTS: TABLES TO CREATE - LIST
    '''

    try:
        for query in tables:
            exec_query(query, cur)
            logging.debug('Table has been created')
    except:
        logging.error('Already created. Moving on...')


def insert_records(con, cur, records):

    '''
    INSERTS RECORDS TO TABLES
    ARGUMENTS: CON - CONNECTION TO DATABASE
                RECORDS - LIST OF RECORDS TO INSERT
    '''

    try:
        for insert in records:
            exec_query(insert, cur)
            logging.debug('Record has been inserted')
    except:
        logging.error('Already inserted. Moving on...\n')
    con.commit()

def get_headers(cur, query):

    '''
    PRINTS THE HEADERS OF ALL TABLES
    '''

    cur.execute(query)
    return list(map(lambda x: x[0], cur.description))

def main():

    print('My Movie Database\n')

    # DEFINES DATABASE, MAKES CONNECTION, AND GETS CURSOR OBJECT
    database = 'movies_assignment3c.db'
    con = connect_db(database)
    logging.debug(f'Connected to {database}...')
    cur = con.cursor()

    # # SET QUERY, EXECUTE, AND FETCH
    table1query = '''
    CREATE TABLE movies_info_1 (
	show_id INT PRIMARY KEY,
	genre varchar,
	title varchar,
    director varchar);'''

    table2query = '''
    CREATE TABLE movies_info_2 (
	show_id INT,
    release_year INT,
	description varchar);'''

    table_queries = [table1query, table2query]
    create_table(table_queries, cur)

    # INSERTING INTO TABLES
    # MOVIES_INFO_1
    inserttable1query1 = """
    INSERT INTO movies_info_1(show_id, genre, title, director)
    VALUES (1, 'Adventure/Action', 'Lara Croft: Tomb Raider',  'Simon West')"""
    inserttable1query2 = """
    INSERT INTO movies_info_1(show_id, genre, title, director)
    VALUES (2, 'Horror/Action', 'Resident Evil', 'Paul W. S. Anderson')"""
    inserttable1query3 = """
    INSERT INTO movies_info_1(show_id, genre, title, director)
    VALUES (3, 'Comedy/Fantasy', 'Ghostbusters', 'Ivan Reitman')"""

    # MOVIES_INFO_2
    inserttable2query1 = """
    INSERT INTO movies_info_2(show_id, release_year, description)
    VALUES (1, 2001, 'This live action feature is inspired by the most successful\
    interactive video-game character in history -- Lara Croft.')"""
    inserttable2query2 = """
    INSERT INTO movies_info_2(show_id, release_year, description)
    VALUES (2, 2002, 'Based on the popular video game, Milla Jovovich and\
    Michelle Rodriguez star as the leaders of a commando team who must break into "the hive,"\
    a vast underground genetics laboratory operated by the powerful Umbrella Corporation.')"""
    inserttable2query3 = """
    INSERT INTO movies_info_2(show_id, release_year, description)
    VALUES (3, 1984, '''After the members of a team of scientists (Harold Ramis, Dan Aykroyd, Bill Murray)\
    lose their cushy positions at a university in New York City, they decide to become "ghostbusters" \
    to wage a high-tech battle with the supernatural for money.''')"""

    all_insert = [inserttable1query1, inserttable1query2, inserttable1query3,
                    inserttable2query1, inserttable2query2, inserttable2query3]
    insert_records(con, cur, all_insert)

    # JOIN
    join_query = """
    SELECT genre, title, director, release_year, description
    FROM movies_info_1
    JOIN movies_info_2
    ON movies_info_1.show_id = movies_info_2.show_id"""

    movie_data = exec_query(join_query, cur)

    # GET HEADERS
    col_names = get_headers(cur, join_query)

    # DISPLAY DATA
    print(f'{col_names[0]}\t\t{col_names[1]}\t\t{col_names[2]}\t\t{col_names[3]}\t\t{col_names[4]}')
    for movie in movie_data:
        print(f'{movie[0]}\t{movie[1]}\t{movie[2]}\t{movie[3]}\t{movie[4]}')

    # CLOSE THE CONNECTION
    if con:
        con.commit()
        con.close()
        print()
        logging.debug(f'{database} has been closed...')

    print('That\'s all folks. See You Soon!')

if __name__ == '__main__':
    main()