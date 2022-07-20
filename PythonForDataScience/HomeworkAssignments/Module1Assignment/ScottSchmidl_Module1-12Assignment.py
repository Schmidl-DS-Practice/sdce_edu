#!/usr/bin/env python3

# COMP 699 - Python for Data Science - 06/21/2021 to 08/21/2021 - Section 1.12 Module 1 Assignment
# Author: Scott Schmidl

import pandas as pd

def loadData(filename:str) -> pd.DataFrame:
    return  pd.read_csv(filename)

def subSet(df:pd.DataFrame, cylinders:int) -> pd.DataFrame:
    df_cyl = df[df["cyl"] == cylinders]
    print(df_cyl.shape)

def main():
    filename = "../csvfiles/mtcars.csv"
    df = loadData(filename)

    cylinders = int(input())
    subSet(df, cylinders)

if __name__ == "__main__":
    main()