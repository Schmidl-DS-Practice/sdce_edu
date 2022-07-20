#Scott Schmidl - COMP 660 - Programming with Python I - 02/01/2021 to 04/10/2021 - Section 6.4 Module 6 Assignment

#Question 6
full_name = input('Enter your first name, middle name, and lastname name? ')
full_name_firstspace = full_name.find(' ')
full_name_secondspace = full_name.find(' ', full_name_firstspace+1)

middle_name = full_name[full_name_firstspace+1:full_name_secondspace]
mid_abbrevated = middle_name.replace(middle_name[1:], '.').capitalize()

print(f'{full_name[:full_name_firstspace]} {mid_abbrevated} {full_name[full_name_secondspace+1:]}')
