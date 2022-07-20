#Scott Schmidl - COMP 660 - Programming with Python I - 02/01/2021 to 04/10/2021 - Section 3.4 Module 3 Assignment

#Question 3

for i in range(2):

    def tshirt_sweater(name, temp):
        if temp >= 70: print(f'Hi {name}, It will be a warm day, T-shirt time!')
        else: print(f'Hi {name}, You should probably bring a sweater')

    name=input('\nPlease Enter Your First Name: ')
    temp=int(input('What is Today\'s Temperature: '))
    tshirt_sweater(name=name, temp=temp)
