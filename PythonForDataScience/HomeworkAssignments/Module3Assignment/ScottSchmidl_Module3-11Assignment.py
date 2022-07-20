#!/usr/bin/env python3

# COMP 699 - Python for Data Science - 06/21/2021 to 08/21/2021 - Section 3.11  Module 3 Assignment
# Author: Scott Schmidl

from statsmodels.formula.api import ols
import statsmodels.api as sm
import pandas as pd

def loadData(filename:str) -> pd.DataFrame:
    return  pd.read_csv(filename)

def newCol(df:pd.DataFrame, col:list) -> pd.DataFrame:
    df[col[0]] = df[col[1]] - df[col[2]]
    return df

def getStats(df:pd.DataFrame, olsString:str) -> tuple:
    results = ols(olsString, data=df).fit()
    aov_table =  sm.stats.anova_lm(results, typ=2)

    return results.summary(), aov_table

def main():

    filename = "../csvfiles/nbaallelo_slr.csv"
    df = loadData(filename)

    # print(df.head())
    # print(df.info())

    col = ["y", "pts", "opp_pts"]
    newDf = newCol(df, col)
    # print(newDf.head())
    # print(newDf.info())

    olsString = "y ~ elo_i"
    # olsString1 = "y ~ elo_n"
    resSum, aov_table = getStats(newDf, olsString)
    print(resSum)
    print(aov_table)

if __name__ == "__main__":
    main()