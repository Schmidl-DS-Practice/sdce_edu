#!/usr/bin/env python3

# COMP 699 - Python for Data Science - 06/21/2021 to 08/21/2021 - Section 1.15 Module 1 Assignment
# Author: Scott Schmidl

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set(style="darkgrid")

def loadData(filename:str) -> pd.DataFrame:
    return  pd.read_csv(filename)

def subSet(df:pd.DataFrame) -> pd.DataFrame:
    return df.loc[(df['sex'] == "male") & (df['pclass'] == 1) & (df['age'] > 18)]

def stripPlot(df:pd.DataFrame):
    saveIt = "town_survived.png"
    label = ["No","Yes"]
    lTitle = "Survived"

    _, ax = plt.subplots()
    sns.stripplot(x="embark_town", y="age", data=df, hue="survived")
    plt.xlabel("\nEmbark Town")
    plt.ylabel("Age")
    legend_labels, _= ax.get_legend_handles_labels()
    plt.legend(legend_labels, label, title=lTitle)
    plt.tight_layout()
    # plt.savefig(saveIt)
    plt.show()

def main():
    filename = "../csvfiles/titanic.csv"
    titanic = loadData(filename)

    titanicSub = subSet(titanic)
    # print(titanicSub.head())

    stripPlot(titanicSub)

if __name__ == "__main__":
    main()