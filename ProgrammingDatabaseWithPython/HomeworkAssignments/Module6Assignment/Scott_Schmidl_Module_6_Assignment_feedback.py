#!/usr/bin/env python3
# Module 6 Assignment - COMP 662 - Programming Databases with Python - 04/12/2021 to 06/10/2021
# Author: Scott Schmidl

import matplotlib.pyplot as plt
import sqlite3
import logging
import os
from ClassSQLite import ClassSQLite as eql

def plot_query(majors,plotname):
    """PLOT QUERY RESULTS

    Args:
        plotname (STRING): NAME OF THE PLOT
        majors (LIST): LIST OF STRINGS FOR LEGEND
    """
    plt.title(plotname, fontsize=8)
    plt.xlabel('Year', fontsize=8)
    plt.ylabel('Degrees', fontsize=8)
    plt.tight_layout()
    plt.legend(majors, fontsize=8)
    plt.show()

def main():
    filename = 'degrees.db'
    pltname = "% of Bachelor's Degrees for USA Women by Major (1970-2011)\n\nDegrees Over Time"
    majors = ['HealthProfessions', 'Education', 'ComputerScience', 'Engineering']

    mysql = eql(filename,'Degrees')
    # CHECK FILE EXISTS

    if mysql.db_checkfile():
        # ATTEMPT QUERY EXECUTION AND PLOT RESULTLS
        try:
            mysql.db_connect()
            mysql.db_cursor()
            years = mysql.db_runquery("""select year from 'percent-bachelors-degrees-women-usa';""")

            for major in majors:
                query =   "select " + major + """ from 'percent-bachelors-degrees-women-usa';"""
                x_query_result = mysql.db_runquery(query)
                plt.plot(years, x_query_result)
            plot_query(majors, pltname)

        except sqlite3.Error as error:
            logging.error(f"Unsuccessful, error executing query. {error}")

        # CLOSE DATABASE
        finally:
            mysql.db_close()
        print('Done - Thanks for checking out the database.')
        logging.info("Completed.")

if __name__ == "__main__":
    main()
