#!/usr/bin/env python3

# COMP 699 - Python for Data Science - 06/21/2021 to 08/21/2021 - Section 1.11 Module 1 Assignment
# Author: Scott Schmidl

import pandas as pd

def loadData(filename:str) -> pd.DataFrame:
    return  pd.read_csv(filename)

def maxValues(df:pd.DataFrame, userNum:int) -> pd.Series:
    print(df[:userNum].max())


def main():
    filename = "../csvfiles/Cars.csv"
    cars_df = loadData(filename)

    userNum = int(input())
    maxValues(cars_df, userNum)

if __name__ == "__main__":
    main()