#Scott Schmidl - COMP 660 - Programming with Python I - 02/01/2021 to 04/10/2021 - Section 5.3 Module 5 Assignment

#Question 2
def factorial(n):

    if n == 0 or n == 1: return 1

    else: return n * factorial(n-1)

for i,v in enumerate(range(5)):
    print(v, factorial(i))

