#Scott Schmidl - COMP 660 - Programming with Python I - 02/01/2021 to 04/10/2021 - Section 6.4 Module 6 Assignment

#Question 2
def find_strip(s='inet addr:127.0.0.1  Mask:255.0.0.0'):

    '''find a character in s, slices into it,
    and right strips trailing characters

    s -> type string
    '''

    find_me = s.find(':')

    return s[find_me+1:].rstrip()

u = find_strip()
print(u)

