#Scott Schmidl - COMP 660 - Programming with Python I - 02/01/2021 to 04/10/2021 - Section 3.4 Module 3 Assignment

#Question 1
print("""Pass: Used as a place holder or reminder. For example, if one wants to create a "for loop" or a "class",
but one does not have anything to run inside, one could use pass so that the code does not execute and create an error.""")

class assignment():
    pass

for i in range(10):
    pass

print("""\nContinue: Used to move on to the next iteration in a loop, if a certain condition is met.""")
for i in range(10):
    if i == 5: #5 will not be printed to do the following continue statement
        continue
    else: print(i)
