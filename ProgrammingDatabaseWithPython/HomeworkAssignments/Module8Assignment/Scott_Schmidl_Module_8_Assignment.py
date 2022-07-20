#!/usr/bin/env python3

# Module 8 Assignment - COMP 662 - Programming Databases with Python - 04/12/2021 to 06/10/2021
# Author: Scott Schmidl

from ClassSQLite import EsQuLite as eql
import matplotlib.pyplot as plt
import pandas as pd
import logging

def beer_data(query, con):
    """GET DATAFRAME FROM SQL DATABASE TABLE

    Args:
        query (STRING): QUERY TO TABLE
        con (OBJECT): CONNECTION TO DATABASE

    Returns:
        PANDAS DATAFRAME: DATAFRAME TO ANALYZE
    """

    try:
        beer_df = pd.read_sql_query(query, con)
        return beer_df
    except:
        logging.error("Not able to ready SQL")

def quest1_3(df):
    """PRINTS ANSWERS FOR QUESTIONS 1 TO 3

    Args:
        df (PANDAS DATAFRAME): DF TO ANALYZE
    """

    print(f"\nQ1) How many rows are in the table?\n{len(df)}")
    print(f"\nQ2) Describe the table:\n{df.describe()}")
    print(f"\nQ3) How many entries are there for each brewery?\n{df.groupby(['brewery_name']).size()}")

def create_abv(df):
    """CREATE NEW DATAFRAME

    Args:
        df (PANDAS DATAFRAME): DF TO SUBQUERY

    Returns:
        DATAFRAME: NEW DATAFRAME
    """

    return df[df.beer_abv < 1]

def quest4_6(df):
    """PRINTS ANSWERS FOR QUESTIONS 4 TO 6

    Args:
        df (PANDAS DATAFRAME): DF TO ANALYZE
    """

    print(f"\nQ4) Find all entries with low alcohol. Alcohol by volume (ABV) less than 1%:\n{df}")
    print(f"\nQ5) How many reviews are there for low ABV beers?\n{len(df)}")
    print(f"\nQ6) Group  the AVB beers by beer and count: \n{df.groupby('beer_name').size()}")

def o_hist(series):
    """HISTOGRAM PLOT

    Args:
        series (PANDAS SERIES): SERIES TO PLOT

    Returns:
        FLOAT: MEAN AND STD OF SERIES
    """

    try:
        series.hist()
        plt.savefig(('odouls_hist.png'))
        plt.show()
    except:
        logging.error("Could not create histogram from series")

    return series.mean(), series.std()

def quest7_9(series):
    """PRINTS ANSWERS FOR QUESTIONS 7 TO 9

    Args:
        series (PANDAS SERIES): SERIES TO ANALYZE
    """

    print(f"\nQ7) How consistent are the O'Douls overall scores?\n{series}")
    print(f"\nQ8) Plot a histogram of O'Douls overall scores (may need to close window to continue):\nSee Plot")
    o_mean, o_std = o_hist(series)
    print(f"\nQ9) For O'Douls, what are the mean and standard deviation for the O'Doul's overall scores?")
    print(f"O'Doul's Mean: {o_mean}\nO'Doul's STD: {o_std}")

def abv_boxplot(df):
    """BOX PLOT

    Args:
        df (PANDAS DATAFRAME): DATAFRAME TO PLOT
    """

    try:
        df.boxplot(fontsize=10, figsize=(12,10))
        plt.savefig(('abv_boxplot.png'))
        plt.show()
    except:
        logging.error("Could not create box plot from df")

def quest10(df):
    """PRINTS ANSWER TO QUESTION 10

    Args:
        df (PANDAS DATAFRAME): DF TO ANALYZE
    """

    print(f"\nQ10) Draw a boxplot of the low_abv data (may need to close window to continue):\nSee Plot")
    abv_boxplot(df)

def main():
    # GET CONNECTION AND CURSOR
    filename = "beers.db"
    db_title = "beers"
    to_perform = eql(filename, db_title)
    con = to_perform.db_connect()

    # QUERY TO GET SQL TABLE
    beers_query = """
    SELECT *
    FROM reviews"""
    beer_df = beer_data(beers_query, con)

    # QUESTIONS 1-3: USE BEER_DF
    quest1_3(beer_df)

    # QUESTIONS 4-6: USE LOW_ABV
    low_abv = create_abv(beer_df)
    quest4_6(low_abv)

    # QUESTIONS 7-9: USE ODOULS
    odouls = low_abv[low_abv.beer_name == "O'Doul's"]['review_overall']
    quest7_9(odouls)

    # QUESTION 10: USES LOW_ABV
    quest10(low_abv)

    if con: to_perform.db_close()

if __name__ == "__main__":
    main()