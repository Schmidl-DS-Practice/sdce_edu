#!/usr/bin/env python3

# COMP 699 - Python for Data Science - 06/21/2021 to 08/21/2021 - Section 1.10 Module 1 Assignment
# Author: Scott Schmidl

import numpy as np
import scipy.stats as st

def linreg(x1:int, x2:int , x3:int, x4:int):

    x = np.array([x1, x2, x3, x4])
    y = np.array([0, 10, 7, 25])

    print(st.linregress(x,y))

def main():
    x1 = int(input())
    x2 = int(input())
    x3 = int(input())
    x4 = int(input())

    linreg(x1, x2, x3, x4)

if __name__ == "__main__":
    main()
