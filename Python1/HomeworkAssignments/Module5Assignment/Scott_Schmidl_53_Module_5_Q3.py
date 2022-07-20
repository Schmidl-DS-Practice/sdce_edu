#Scott Schmidl - COMP 660 - Programming with Python I - 02/01/2021 to 04/10/2021 - Section 5.3 Module 5 Assignment

#Qeustion 3
def sum_to_n(n):

    if n == 0: return 0

    elif n == 1: return 1

    else: return n + sum_to_n(n-1)

for i,v in enumerate(range(10)):
    print(v, sum_to_n(i))