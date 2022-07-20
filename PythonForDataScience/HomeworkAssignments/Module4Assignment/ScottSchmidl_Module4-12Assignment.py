#!/usr/bin/env python3

# COMP 699 - Python for Data Science - 06/21/2021 to 08/21/2021 - Section 4.12  Module 4 Assignment
# Author: Scott Schmidl

from sklearn import preprocessing as pp
import pandas as pd

def loadData(filename:str) -> pd.DataFrame:
    return  pd.read_csv(filename)

def standNorm(df:pd.DataFrame, cols:list):
    hmeqStand = pd.DataFrame(pp.scale(df),columns=cols)
    hmeqNorm = pd.DataFrame(pp.MinMaxScaler().fit_transform(df), columns=cols)

    return hmeqStand, hmeqNorm

def main():

    filename = "../csvfiles/hmeq_lab412.csv"
    hmeq = loadData(filename)
    # print(hmeq.info())

    cols = list(hmeq.columns.values)
    hmeqStand, hmeqNorm = standNorm(hmeq, cols)
    print(f"The means of hmeqStand are\n{hmeqStand.mean()}")
    print(f"The standard deviations of hmeqStand are\n{hmeqStand.std()}")
    print(f"The means of hmeqStand are\n{hmeqNorm.mean()}")
    print(f"The standard deviations of hmeqStand are\n{hmeqNorm.std()}")

if __name__ == "__main__":
    main()
