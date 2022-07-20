#!/usr/bin/env python3

# COMP 699 - Python for Data Science - 06/21/2021 to 08/21/2021 - Section 4.11  Module 4 Assignment
# Author: Scott Schmidl

import pandas as pd

def loadData(filename:str) -> pd.DataFrame:
    return  pd.read_csv(filename)

def subSet(df:pd.DataFrame):

    missDataDel = df.dropna(axis=0)
    missDataFill = df.fillna(df.mean(), axis=0)

    return missDataDel.mean(), missDataFill.mean()

def main():

    # pd.options.mode.use_inf_as_na = True

    filename = "../csvfiles/hmeq_small.csv"
    hme = loadData(filename)
    # print(hme.info())

    # cols = [hme.isnull().any(axis=1)]
    # print(type(hme.mean()))
    missDataDelM, missDataFillM = subSet(hme)
    print(f"Means for missDataDelM are\n{missDataDelM}")
    print(f"Means for missDataFillM are\n{missDataFillM}")

if __name__ == "__main__":
    main()