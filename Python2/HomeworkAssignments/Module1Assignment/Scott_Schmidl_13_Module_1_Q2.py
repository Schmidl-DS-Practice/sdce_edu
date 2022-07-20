# Scott Schmidl - COMP 661 - Programming with Python II - 04/12/2021 to 06/10/2021 - Section 1.3 Module 1 Assignment

from datetime import datetime as dt

def get_birthday():

    '''
    RETURNS NAME AND BDAY AS STRINGS
    '''

    name = input('Enter Name: ')
    bday = input('Enter Birthday (MM/DD/YY): ')

    return name, bday

def dt_converts(bday):

    '''
    RETURNS THE BIRTH DATE AND TODAY'S DATE AS DATETIME OBJECTS
    '''

    bday_conv = dt.strptime(bday, '%m/%d/%y')
    bday_dt = bday_conv.strftime('%A, %B %d, %Y')
    today = dt.today().strftime('%A, %B %d, %Y')

    return bday_dt, today

def get_age(bday_dt, today):

    '''
    RETURNS THE CURRENT AGE OF THE PERSON IN QUESTION
    '''

    bday_dt = dt.strptime(bday_dt, '%A, %B %d, %Y')
    today = dt.strptime(today, '%A, %B %d, %Y')
    age = round((today - bday_dt).days / 365.25, 2)

    return bday_dt, today, age

def time_to_next(next_bd, today):

    '''
    RETURNS THE TIME UNTIL THE PERSON'S NEXT BIRTHDAY
    '''

    if today > next_bd:
        next_year = today.year + 1
        next_bd = dt(next_year, next_bd.month, next_bd.day)
    time_to_next_bday = (next_bd - today).days

    return time_to_next_bday

def main():

    '''
    RUNS THE FUNCTIONS AND PRINTS NAME, BIRTH DATE, AGE, AND TIME UNTIL BIRTHDAY
    '''

    print('Birthday Calculator')

    while True:

        #FUNCTION TO GET NAME AND BIRTH DATE
        name, bday = get_birthday()

        #FUNCTION TO CONVERT TO DATETIME
        bday_dt, today = dt_converts(bday)
        print(f'Birthday: {bday_dt}')
        print(f'Today: {today}')

        #FUNCTION TO GET THE AGE
        bday_dt, today, age = get_age(bday_dt, today)
        print(f'{name} is {age} years old.')
        next_bday = dt(today.year, bday_dt.month, bday_dt.day)

        #FUNCTION TO GET DAYS UNTIL NEXT BDAY
        time_to_next_bday = time_to_next(next_bday, today)
        if time_to_next_bday == 0:
            print(f'{name}\'s birthday is today!\n')
        else:
            print(f'{name}\'s birthday is in {time_to_next_bday} days\n')

        #TO CONTINUE WHILE LOOP
        cont = input('Continue? (y/n): ').lower()
        print()

        if cont == 'n':
            print('Bye!')
            break

if __name__ == '__main__':
    main()