#!/usr/bin/env python3

# COMP 699 - Python for Data Science - 06/21/2021 to 08/21/2021 - Section 3.13  Module 3 Assignment
# Author: Scott Schmidl

import pandas as pd

def loadData(filename:str) -> pd.DataFrame:
    return  pd.read_csv(filename)

def subSet(df:pd.DataFrame, cols:list):
    return df[cols]

def newCol(df:pd.DataFrame, col:list) -> pd.DataFrame:
    df[col[0]] = df[col[1]] - df[col[2]]
    return df

def corrMatrix(df:pd.DataFrame):
    print(df.corr())

def main():

    filename = "../csvfiles/nbaallelo_slr.csv"
    nba = loadData(filename)
    # print(nba.info())

    # eloiCol = ["elo_i", "pts", "opp_pts"]
    elonCol = ["elo_n", "pts", "opp_pts"]
    # nbaSub1 = subSet(nba, eloiCol)
    nbaSub2 = subSet(nba, elonCol)
    # print(nbaSub1.info())
    # print(nbaSub2.info())

    col2 = ["y", "pts", "opp_pts"]
    newNBAdf = newCol(nba, col2)
    # print(newNBAdf.info())

    # corCols = ["elo_i", "y"]
    corCols2 = ["elo_n", "y"]
    corrMatrix(nbaSub2)
    corrMatrix(newNBAdf[corCols2])

if __name__ == "__main__":
    main()