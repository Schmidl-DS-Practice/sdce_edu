#!/usr/bin/env python3

# COMP 699 - Python for Data Science - 06/21/2021 to 08/21/2021 - Section 1.14 Module 1 Assignment
# Author: Scott Schmidl

import matplotlib.pyplot as plt
import pandas as pd

def loadData(filename:str) -> pd.DataFrame:
    return  pd.read_csv(filename)

def subSet(df:pd.DataFrame) -> pd.DataFrame:

    # target["Date"] = pd.to_datetime(target["Date"])
    tgt_march = df.tail(19)
    tgt_vol = tgt_march[["Date", "Volume"]]
    tgt_close = tgt_march[["Date", "Close"]]

    return tgt_march, tgt_vol, tgt_close

def vol_close(march:pd.DataFrame, vol:pd.DataFrame, close:pd.DataFrame) -> tuple:

    day = int(input()) - 1

    volume_row = vol.iloc[[day]]
    volume = volume_row.iloc[0][1]

    close_row = close.iloc[[day]]
    close = close_row.iloc[0][1]

    date = march.iloc[[day]].iloc[0][0]

    return volume, close, date

def lineChart(tgt_vol, tgt_close, datesList):

    yticks1 = [5e6,10e6,15e6,20e6]
    yticks2 = [68,70,72,74]

    _, ax = plt.subplots()
    plt.plot(tgt_vol["Date"], tgt_vol["Volume"], label="Volume" )
    plt.title("March 2018 Trading Volume for Target Stock")
    plt.xlabel("Date")
    plt.xticks(datesList, rotation=45)
    plt.ylabel("Number of Trades")
    plt.yticks(yticks1)
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.savefig("Trading_Volume.png")
    plt.show()

    plt.plot(tgt_close["Date"], tgt_close["Close"], label="Price" )
    plt.title("March 2018 Market Closing Price for Target Stock")
    plt.xlabel("Price")
    plt.xticks(datesList, rotation=45)
    plt.ylabel("Date")
    plt.yticks(yticks2)
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.savefig("Closing_Price.png")
    plt.show()

def main():
    filename = "../csvfiles/target.csv"
    target = loadData(filename)
    datesList = target.tail(19)["Date"].to_list()[1::4]

    tgt_march, tgt_vol, tgt_close = subSet(target)

    volume, close, date = vol_close(tgt_march, tgt_vol, tgt_close)

    print(f"The volume of TGT on {date} is {round(volume)}.")
    print(f"The closing stock price of TGT on {date} is ${close}.")

    lineChart(tgt_vol, tgt_close, datesList)

if __name__ == "__main__":
    main()