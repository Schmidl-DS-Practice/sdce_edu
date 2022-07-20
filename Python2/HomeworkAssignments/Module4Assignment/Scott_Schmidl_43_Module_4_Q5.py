# Scott Schmidl - COMP 661 - Programming with Python II - 04/12/2021 to 06/10/2021 - Section 4.2 Module 4 Assignment

filename = 'accounts.txt'
lines_to_write = ['100 Mary 34.58\n', '200 Alison 345.67\n', '300 Marc 3.00\n',\
                    '400 Zoltar -32.16\n', '500 Kathleen 24.32']
with open(filename, 'w') as accounts:
    print('accounts.txt has been created')
    accounts = accounts.writelines(lines_to_write)
    print('accounts.txt has been written too')
