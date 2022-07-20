# Scott Schmidl - COMP 661 - Programming with Python II - 04/12/2021 to 06/10/2021 - Section 4.2 Module 4 Assignment

import os

print('Commence question 6')

filename = 'accounts.txt'
with open(filename, 'r') as accounts:
    accountsdata  = accounts.read()

accountsdata = accountsdata.replace('Zoltar', 'Robert')

newfilename = 'tempfile.txt'
with open (newfilename, 'w') as tempfile:
    tempfile.write(accountsdata)

filetoremove = 'accounts.txt'
renamedfile = 'myaccounts.txt'

os.remove(filetoremove)

os.rename(newfilename, renamedfile)

print('Congrats you have created myaccounts.txt')