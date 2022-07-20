#!/usr/bin/env python3

# Module 6 Assignment - COMP 662 - Programming Databases with Python - 04/12/2021 to 06/10/2021
# Author: Scott Schmidl

import matplotlib.pyplot as plt
import sqlite3
import logging
import os

def debug_config(title):
    """SETS CONFIGURATION FOR LOGGING

    Args:
        title (STRING): TITLE FOR DEBUGGING OUTPUT
    """

    logging.basicConfig(level=logging.DEBUG,format=f"[{title}]: %(asctime)s: %(levelname)s: %(message)s")
    logging.getLogger('matplotlib.font_manager').disabled = True

def db_checkfile(filename):
    """CHECKS DATABASE EXISTS

    Args:
        filename (STRING): .SQLITE OR .DB FILE

    Returns:
        BOOLEAN DEPENDING ON IF DATABASE EXISTS
    """

    if os.path.exists(filename) and os.path.getsize(filename) > 0:
        logging.debug(f"{filename} found and not zero size.")
        return True
    else:
        logging.error(f"{filename} not found or zero size.")
        return False

def db_connect(filename):
    """CONNECTS TO DATABASE

    Args:
        filename (STRING): .SQLITE OR .DB FILE

    Returns:
        CONNECTION OBJECT: CONNECTION TO THE DATABASE
    """

    con = sqlite3.connect(filename)
    logging.debug("Successfully Connected to Database...")
    return con

def db_cursor(con):
    """SETS THE CURSOR OBJECT

    Args:
        con (OBJECT): CONNECTION TO THE DATABASE

    Returns:
        CURSOR OBJECT: CURSOR OBJECT ON WHICH SQL QUERIES CAN BE EXECUTED
    """

    cur = con.cursor()
    logging.debug("Cursor has been set.\n")
    return cur

def db_runquery(cur, query):
    """RUN A QUERY

    Args:
        cur (CURSOR OBJECT): THE CURSOR OBJECT ON WHICH SQL QUERIES CAN BE EXECUTED
        query (STRING): SQL QUERY TO EXECUTE

    Returns:
        LIST: RESULTS FROM THE QUERY
    """

    cur.execute(query)
    result = cur.fetchall()
    logging.debug("Successfully executed and returned query")
    return result

def plot_query(x, y, plotname, x_ticks, y_ticks, legend_labels):
    """PLOT QUERY RESULTS

    Args:
        x (LIST): X_AXIS DATA
        y (LIST)): Y-AXIS DATA
        plotname (STRING): NAME OF THE PLOT
        x_ticks (LIST): LISTS OF INTEGERS FOR X TICKS
        y_ticks (LIST): LISTS OF INTEGERS FOR Y TICKS
        legend_labels (LIST): LIST OF STRINGS FOR LEGEND
    """

    plt.plot(x, y)
    plt.title(plotname, fontsize=8)
    plt.xlim((1968, 2013))
    plt.ylim((-5, 90))
    plt.xticks(x_ticks, fontsize=8)
    plt.yticks(y_ticks, fontsize=8)
    plt.xlabel('Year', fontsize=8)
    plt.ylabel('Degrees', fontsize=8)
    plt.tight_layout()
    plt.legend(legend_labels, fontsize=8)
    #plt.savefig('USA_Women_BD.png')
    plt.show()

def main():

    # VARIABLES FOR PLOT
    pltname = "% of Bachelor's Degrees for USA Women by Major (1970-2011)\n\nDegrees Over Time"
    legend_labels = ['HealthProfessions', 'Education', 'ComputerScience', 'Engineering']
    x_ticks = [1970, 1980, 1990, 2000, 2010]
    y_ticks = [0, 20, 40, 60, 80]

    # VARIABLES TO CONNECT TO DATABASE AND ACCESS TABLE FOR QUERY
    filename = 'degrees.db'
    log_title = 'Degrees'

    # SET BASIC LOGGING CONFIG
    debug_config(log_title)

    # CHECK FILE EXISTS
    if db_checkfile(filename):
        con = db_connect(filename)
        cur = db_cursor(con)

        # ATTEMPT QUERY EXECUTION AND GET X & Y DATA
        try:
            x_query= """
            SELECT Year, HealthProfessions, Education, ComputerScience, Engineering
            FROM 'percent-bachelors-degrees-women-usa';"""
            x_query_result = db_runquery(cur, x_query)
            lst_xdata = [data[0] for data in x_query_result]
            lst_ydata = [data[1:] for data in x_query_result]
        except sqlite3.Error as error:
            logging.error(f"Unsuccessful, error executing query. {error}")

        # CLOSE DATABASE AND PLOT RESULTS
        finally:
            if con:
                con.close()
                print()
                logging.debug("Database has been closed...")
                plot_query(lst_xdata, lst_ydata, pltname, x_ticks, y_ticks, legend_labels)

        print('Done - Thanks for checking out the database.')
        logging.info("Completed.")

if __name__ == "__main__":
    main()
