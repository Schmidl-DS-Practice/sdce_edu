#!/usr/bin/env python3

# COMP 699 - Python for Data Science - 06/21/2021 to 08/21/2021 - Section 2.9 Module 2 Assignment
# Author: Scott Schmidl

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def loadData(filename:str) -> pd.DataFrame:
    return  pd.read_csv(filename)

def subSetDF(df:pd.DataFrame, cols:list) -> pd.DataFrame:
    return df[cols]

def getPop(df:pd.DataFrame, row:int) -> int:
    return df.iloc[row]

def boxPlot(df:pd.DataFrame):

    mean = round(df["Population"].mean(), 2)
    saveit = "Module2-9BoxPlot.png"

    sns.boxplot(y="Population", data=df, width=0.35, meanline=True)
    plt.axhline(df["Population"].mean(), color="r", ls="--")
    plt.text(0.19, 0.73e7, f"Mean: {mean:,}", bbox=dict(facecolor="white", alpha=0.5))
    plt.ylabel("Population in 10 Millions")
    plt.tight_layout()
    plt.savefig(saveit)
    plt.show()

def main():

    filename = "../csvfiles/internetusage.csv"
    df = loadData(filename)
    # print(df.info())

    cols = ["State", "Population"]
    population = subSetDF(df, cols)
    print(population.head())
    print(population.mean())

    row = int(input("Enter a Row an Integer: "))
    state_data = getPop(population, row)
    print(f"The population of {state_data[0]} is {state_data[1]}.")

    boxPlot(population)


if __name__ == "__main__":
    main()