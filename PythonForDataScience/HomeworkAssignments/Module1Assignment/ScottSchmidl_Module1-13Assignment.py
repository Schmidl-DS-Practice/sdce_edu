#!/usr/bin/env python3

# COMP 699 - Python for Data Science - 06/21/2021 to 08/21/2021 - Section 1.13 Module 1 Assignment
# Author: Scott Schmidl

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def loadData(filename:str) -> pd.DataFrame:
    return  pd.read_csv(filename)

def subSet(df:pd.DataFrame) -> pd.DataFrame:
    firstSouth = df.loc[(df['pclass'] == 1) & (df['embarked'] == "S")]
    secondThird = df[df["pclass"].isin([2, 3])]
    return firstSouth, secondThird

def firstSbarplot(data:list, llabel:list):

    y_ticks = [0, 20, 40, 60, 80]

    _, ax = plt.subplots()
    plt.bar(["female"], data[1], 0.3)
    plt.bar(["male"], data[0], 0.3)
    plt.xticks("")
    plt.yticks(y_ticks)
    plt.xlabel("First\nPassenger Class")
    plt.ylabel("Count")
    plt.legend(llabel, bbox_to_anchor=(1.24, 1), loc="upper right")
    plt.grid(alpha=0.3)
    plt.tight_layout()
    # plt.savefig("HomeworkAssignments/Module1Assignment/first_class_southampton.png")
    plt.show()

def sec_third_barplot(surv:list, notsurv:list):

    labels = ["Second", "Third"]
    y_ticks = [0, 100, 200, 300]
    # THE LABEL LOCATIONS
    x = np.arange(len(labels))
    width = 0.3

    fig, ax = plt.subplots()
    ax.bar(x - width/2, surv, width, label='Survived')
    ax.bar(x + width/2, notsurv, width, label='Not Survived')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    plt.yticks(y_ticks)
    plt.xlabel("Passenger Class")
    plt.ylabel("Count")
    plt.grid(alpha=0.3)
    plt.tight_layout()
    ax.legend()
    # plt.savefig("HomeworkAssignments/Module1Assignment/second_third_surv.png")
    plt.show()

def main():
    filename = "../csvfiles/titanic.csv"
    titanic = loadData((filename))

    first_south, second_third = subSet(titanic)
    print(first_south.head())
    print(second_third.head())

    countMale = first_south.loc[(first_south['sex'] == 'male')].count()["class"]
    countFemale = first_south.loc[(first_south['sex'] == 'female')].count()["class"]

    dataFS = [countMale, countFemale]
    fc_label = ["female", "male"]
    firstSbarplot(dataFS, fc_label)

    countSurvived2 = second_third.loc[
        (second_third['survived'] == 1) & (second_third["pclass"] == 2)].count()["pclass"]
    countNotSurvived2 = second_third.loc[
        (second_third['survived'] == 0) & (second_third["pclass"] == 2)].count()["pclass"]
    countSurvived3 = second_third.loc[
        (second_third['survived'] == 1) & (second_third["pclass"] == 3)].count()["pclass"]
    countNotSurvived3 = second_third.loc[
        (second_third['survived'] == 0) & (second_third["pclass"] == 3)].count()["pclass"]

    dataSTsurved = [countSurvived2, countSurvived3]
    dataSTnotsurved = [countNotSurvived2, countNotSurvived3]
    sec_third_barplot(dataSTsurved,  dataSTnotsurved)

if __name__ == "__main__":
    main()