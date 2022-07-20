#Scott Schmidl - COMP 660 - Programming with Python I - 02/01/2021 to 04/10/2021 - Section 5.3 Module 5 Assignment

#Question 1
'''The base case of a recursive function is one where the problem can be solved without further recursion.
If the base case is not meant the function will be stuck in an infinite loop.
'''

#For example, when doing recursion for fibonacci
def fibby(n):

    if n == 0: return 0
    elif n == 1: return 1
    else: return fibby(n-1) + fibby(n-2)

'''In the above example the base case would be if n == 0 or if n == 1.
Without these two outs to the function it would get stuck in an infinite loop.'''

'''Another example would be the if n == 0 or if n == 1 condition for a factorial recursive function.'''