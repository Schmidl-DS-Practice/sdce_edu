# Scott Schmidl - COMP 661 - Programming with Python II - 04/12/2021 to 06/10/2021 - Section 1.3 Module 1 Assignment

from datetime import datetime
from datetime import timedelta

def departure():

    '''
    return - date and time of departure

    arguments - none
    '''

    date_departure = input('Estimated date of departure (YYYY-MM-DD): ')
    time_departure = input('Estimated time of departure (HH:MM AM/PM): ')

    return date_departure, time_departure

def time_hm(miles, velocity):

    '''
    return - duration of travel in hours and minutes

    arguments - miles: int
                velocity: int
    '''

    hours = miles // velocity
    minutes = round(((miles % velocity) / velocity) * 60, 2)

    return hours, minutes

def arrival(date_dep, time_dep, hours, minutes):

    '''
    return - estimated date and time of arrival

    arguments - date_dep: string
                time_dep: string
    '''

    date_time = f'{date_dep} {time_dep}'
    date_time_conv = datetime.strptime(date_time, '%Y-%m-%d %I:%M %p')

    date_time_arrival = date_time_conv + timedelta(hours=hours, minutes=minutes)

    date_arrival = date_time_arrival.date()
    time_arrival = date_time_arrival.time().strftime('%I:%M %p')

    return date_arrival, time_arrival

def main():

    print('Arrival Time Estimator')

    while True:
        date_departure, time_departure = departure()

        miles = int(input('Enter Miles: '))
        velocity = int(input('Enter Miles Per Hour: '))
        hours, minutes = time_hm(miles, velocity)
        print('\nEstimated Travel Time')
        print(f'Hours: {hours}')
        print(f'Minutes: {minutes}')

        date_arrive, time_arrive = arrival(date_departure, time_departure, hours, minutes)
        print(f'Estimated Date of Arrival: {date_arrive}')
        print(f'Estimated Time of Arrival: {time_arrive}')

        cont = input('\nContinue? (y/n): ').lower()

        if cont == 'n':
            print('bye')
            break
        print()
    print()

if __name__ == '__main__':
    main()