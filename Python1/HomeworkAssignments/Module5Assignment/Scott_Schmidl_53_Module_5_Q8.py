####Scott Schmidl - COMP 660 - Programming with Python I - 02/01/2021 to 04/10/2021 - Section 5.3 Module 5 Assignment

from math import log10

###Question 8
ANNUAL_RATE = .0185

MONTHLY_RATE = ANNUAL_RATE / 12

##Part A

doubling_time = lambda rate_of_return: (log10(2)) / (log10(1 + rate_of_return))
print(round(doubling_time(MONTHLY_RATE), 1))

#ANSWER: approximately 450 months which is about 37.8 years

##Part B

doubling_time_yrs = lambda rate_of_return: (log10(2)) / (log10(1 + rate_of_return))
print(round(doubling_time_yrs(ANNUAL_RATE),1))

#ANSWER: approximately 37.8 years which is about 450 months

##Part C

ANNUAL_RATE_C = .03
another_one = lambda rate_of_return: (log10(2)) / (log10(1 + rate_of_return))
print(round(another_one(ANNUAL_RATE_C), 1))

#ANSWER: approximately 23.4 years