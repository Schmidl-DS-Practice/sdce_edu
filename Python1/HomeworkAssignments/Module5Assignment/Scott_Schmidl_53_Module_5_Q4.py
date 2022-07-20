#Scott Schmidl - COMP 660 - Programming with Python I - 02/01/2021 to 04/10/2021 - Section 5.3 Module 5 Assignment

#Question 4

# def semordnilap(aString,index):

#     """
#     this function has an error in the print statement
#     """

#     if index < len(aString):
#         semordnilap(aString, index +1)
#         print(aString[index]), end="")

"""The above function returns an error because of the extra parenthesis in the print statement.
It should look like this:"""

def semordnilap(aString, index):

    if index < len(aString):
        semordnilap(aString, index + 1)
        print(aString[index], end="")

semordnilap('alucard', 0)
print()

"""This function prints out the word "dracula".
Each recursive call stacks up as rows until we reach the base case.
Then, the stack unwinds each row and returns the results from said row."""
