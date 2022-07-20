#!/usr/bin/env python3

# COMP 699 - Python for Data Science - 06/21/2021 to 08/21/2021 - Section 2.7 Module 2 Assignment
# Author: Scott Schmidl

import scipy.stats as st
import pandas as pd

def loadData(filename:str) -> pd.DataFrame:
    return  pd.read_csv(filename)

def subSetDF(df:pd.DataFrame, col:str) -> pd.Series:
    return df[col]

def nbaSTD(ser:pd.Series) -> float:
    return round(st.tstd(ser), 2)

def main():

    filename = "../csvfiles/NBA2019.csv"
    nba = loadData(filename)
    # print(nba.info())

    chosen_column = input("Enter Column: ")
    nba_col = subSetDF(nba, chosen_column)

    stdNBA = nbaSTD(nba_col)
    print(f"The standard deviation for {chosen_column} is: {stdNBA}")

if __name__ == "__main__":
    main()