#!/usr/bin/env python3

# COMP 699 - Python for Data Science - 06/21/2021 to 08/21/2021 - Section 5.4  Module 5 Assignment
# Author: Scott Schmidl

from sklearn.model_selection import train_test_split
from statsmodels.formula.api import logit
import pandas as pd
import numpy as np

def loadData(filename:str) -> pd.DataFrame:
    return  pd.read_csv(filename)

def newDF(df:pd.DataFrame):
    wins = df["game_result"] == "W"
    bool_val = np.multiply(wins, 1)
    winsDF = pd.DataFrame(bool_val, columns = ["game_result"])
    wins_new = winsDF.rename(columns = {"game_result": "wins"})
    return pd.concat([df, wins_new], axis=1)

def logreg(form:str, df:pd.DataFrame):
    train, test = train_test_split(df, test_size=30, train_size=70, random_state=0)
    logModel = logit(formula=form, data=train).fit()
    return logModel.params

def main():

    filename = "../csvfiles/nbaallelo_slr.csv"
    nba = loadData(filename)
    # print(nba.info())
    # print(nba.head())

    newNBA = newDF(nba)
    # print(newNBA.head())

    form = "wins ~ elo_i"
    logCoeff = logreg(form, newNBA)
    print(logCoeff)

if __name__ == "__main__":
    main()