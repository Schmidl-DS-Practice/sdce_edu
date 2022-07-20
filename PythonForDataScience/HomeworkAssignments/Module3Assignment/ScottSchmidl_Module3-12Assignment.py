#!/usr/bin/env python3

# COMP 699 - Python for Data Science - 06/21/2021 to 08/21/2021 - Section 3.12  Module 3 Assignment
# Author: Scott Schmidl

from statsmodels.formula.api import ols
import pandas as pd
import numpy as np

def loadData(filename:str) -> pd.DataFrame:
    return  pd.read_csv(filename)

def getOLS(df:pd.DataFrame, olsString:str):
    return ols(olsString, data=df).fit()

def predictPercIntUs(model,  bachP:float):
    return model.predict(bachP)

def main():

    filename = "../csvfiles/internetusage.csv"
    internet = loadData(filename)
    # print(internet.info())
    # print(internet["bachelors_degree"].head())
    # print(internet["internet_usage"].head())

    olsString = 'internet_usage ~ bachelors_degree'
    model = getOLS(internet, olsString)
    # print(model.summary())

    bach_percent = pd.DataFrame(np.array([float(input("Enter Percent Bachelor's: "))]), columns=["bachelors_degree"])
    prediction = predictPercIntUs(model, bach_percent)
    print(prediction)

if __name__ == "__main__":
    main()