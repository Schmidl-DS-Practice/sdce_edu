#!/usr/bin/env python3

# COMP 699 - Python for Data Science - 06/21/2021 to 08/21/2021 - Section 2.6 Module 2 Assignment
# Author: Scott Schmidl

import pandas as pd

def loadData(filename:str) -> pd.DataFrame:
    return  pd.read_csv(filename)

def carsMMM(df:pd.DataFrame, col:str) -> tuple:
    dfCol = df[col]
    return dfCol.mean(), dfCol.median(), dfCol.mode()

def main():

    filename = "../csvfiles/mtcars.csv"
    mtcars = loadData(filename)
    # print(mtcars.columns)

    wtCol = "wt"
    qsecCol = "qsec"
    mean, median, mode = carsMMM(mtcars, qsecCol)
    print(f"mean = {mean}, median = {median}, mode = {mode}")

if __name__ == "__main__":
    main()