# !/usr/bin/env python3

# COMP 699 - Python for Data Science - 06/21/2021 to 08/21/2021 - Section 2.8 Module 2 Assignment
# Author: Scott Schmidl

import pandas as pd

def loadData(filename:str) -> pd.DataFrame:
    return  pd.read_csv(filename)

# ONE SET OF BRACKETS IS A SERIES
# TWO SETS OF BRACKETS IS A DATAFRAME
def subSetDF(df:pd.DataFrame, col:str) -> pd.Series:
    return df[[col]]

def fiveSummary(ser:pd.Series) -> float:
    print(ser.describe())

def main():

    filename = "../csvfiles/internetusage.csv"
    netUsage = loadData(filename)
    # print(netUsage.info())

    col = "internet_usage"
    internet = subSetDF(netUsage, col)
    # print(internet)

    fiveSummary(internet)

if __name__ == "__main__":
    main()