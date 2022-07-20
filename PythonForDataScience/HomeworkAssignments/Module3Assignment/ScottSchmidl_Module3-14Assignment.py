#!/usr/bin/env python3

# COMP 699 - Python for Data Science - 06/21/2021 to 08/21/2021 - Section 3.14  Module 3 Assignment
# Author: Scott Schmidl

from statsmodels.formula.api import ols
import statsmodels.api as sm
import pandas as pd

def loadData(filename:str) -> pd.DataFrame:
    return  pd.read_csv(filename)

def subSet(df:pd.DataFrame, cols:list):
    return df[cols]

def getStats(df:pd.DataFrame, olsString:str) -> tuple:
    results = ols(olsString, data=df).fit()
    aov_table =  sm.stats.anova_lm(results, typ=2)

    return results.summary(), aov_table

def main():

    filename = "../csvfiles/nbaallelo_slr.csv"
    nba = loadData(filename)

    # cols = ["pts", "opp_pts", "elo_i"]
    cols = ["pts", "opp_pts", "elo_n"]
    subSetNBA = subSet(nba, cols)

    # olsString = "pts ~ elo_i + opp_pts"
    olsString = "pts ~ elo_n + opp_pts"
    results, aov_table = getStats(subSetNBA, olsString)
    # print(results)
    print(aov_table)

if __name__ == "__main__":
    main()