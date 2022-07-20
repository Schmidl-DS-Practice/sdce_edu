#Scott Schmidl - COMP 660 - Programming with Python I - 02/01/2021 to 04/10/2021 - Section 6.4 Module 6 Assignment

#Question 5

num_people = int(input('How many people are here? '))

for _ in range(num_people):

    first_name = input('What is your first name? ')
    last_name = input('What is your last name? ')

    first_name_u = first_name.upper()
    last_name_u = last_name.upper()

    first_name_c = first_name.capitalize()
    last_name_c = last_name.capitalize()

    first_name_t = first_name.title()
    last_name_t = last_name.title()

    print(f'\nHi {first_name_u} {last_name_u}, welcome to my python greet application\n')
    print(f'\nHi {first_name} {last_name}, welcome to my python greet application\n')
    print(f'\nHi {first_name_c} {last_name_c}, welcome to my python greet application\n')
    print(f'\nHi {first_name_t} {last_name_t}, welcome to my python greet application\n')

    '''
    You'll notice that .capitalize(), and .title()
        perform the same action on first_name and last_name because they each have 1 string.
    '''

