#!/usr/bin/env python3

# COMP 699 - Python for Data Science - 06/21/2021 to 08/21/2021 - Section 5.5  Module 5 Assignment
# Author: Scott Schmidl

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix as cm
import pandas as pd
import numpy as np

def loadData(filename:str) -> pd.DataFrame:
    return  pd.read_csv(filename)

def newDF(df:pd.DataFrame):
    wins = df["game_result"] == "W"
    bool_val = np.multiply(wins, 1)
    winsDF = pd.DataFrame(bool_val, columns=["game_result"])
    wins_new = winsDF.rename(columns={"game_result": "wins"})
    return pd.concat([df, wins_new], axis=1)

def logreg(df:pd.DataFrame):
    train, test  = train_test_split(df, test_size=.30, random_state=0)
    x_train = train[["elo_i"]]
    y_train = train["wins"]
    x_test = test[["elo_i"]]
    y_test = test["wins"]

    logModel = LogisticRegression()
    logModel.fit(x_train, y_train)
    y_pred = logModel.predict(x_test)
    return y_pred, y_test

def confuseMatrix(y_pred:np.ndarray, y_test:pd.Series):
    return cm(y_test, y_pred)

def sensSpec(confmat:np.ndarray):
    tp = confmat[1, 1]
    fp = confmat[0, 1]
    tn = confmat[0, 0]
    fn = confmat[1, 0]
    sensitivity = tp / (tp + fn)
    specificity = tn / (tn + fp)
    return sensitivity, specificity

def main():

    filename = "../csvfiles/nbaallelo.csv"
    nba = loadData(filename)
    # print(nba.info())
    # print(nba.head())

    newNBA = newDF(nba)
    # print(len(newNBA))

    y_pred, y_test = logreg(newNBA)

    conMat = confuseMatrix(y_pred, y_test)
    print(f"Confusion Matrix is\n{conMat}")

    sens, spec = sensSpec(conMat)
    print(f"Sensitivity is {sens}")
    print(f"Specificity is {spec}")

if __name__ == "__main__":
    main()