#Scott Schmidl - COMP 660 - Programming with Python I - 02/01/2021 to 04/10/2021 - Section 3.4 Module 3 Assignment

#Question 2
letter = "Hizthere,zThisziszhowzazpasszstatementzworks!"
for i in letter:
    if i == "mn":
        pass
    elif i == "z":
        print(" ",end="")
    else:
        print(i, end='')


print("""\n
The output is 'Hi there, This is how a pass statement works!'""")

print("""
The 'for loop' iterates through each character in the variable letter.
If that character is 'mn' that iteration does nothing and moves on to the next iteration.
If i is 'z' a space is printed and the 'end=""' means print on the same line.
If it is not 'mn' nor 'z', then 'i' is printed and the 'end=''' means print on the same line""")
