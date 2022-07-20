# Scott Schmidl - COMP 660 - Programming with Python I - 02/01/2021 to 04/10/2021 - Section 2.4 Module 2 Assignment

# Question Number 3
def mass_calc(mass=int(input('Enter the mass in pounds(lbs): '))):

    '''
    ask user for their mass

    mass - int

    prints different values involving mass
    '''

    KG = 2.20462 #(kgs)
    mass_kg = mass / KG
    print(f'\nThe converted mass in kgs = {mass_kg} kgs')

    EARTH_GRAVITY = 9.807 #(m/s^2)
    mass_earth_newtons = mass_kg * EARTH_GRAVITY
    print(f'The weight of the mass on Earth (Newtons) = {mass_earth_newtons} Newtons')

    MOON_GRAVITY = 1.62 #(m/s^2)
    mass_moon_newtons = mass_kg * MOON_GRAVITY
    print(f'The weight of the mass on Earth (Newtons) = {mass_moon_newtons} Newtons')

    precent_moon_to_earth = mass_moon_newtons / mass_earth_newtons * 100
    print(f'''The percentage of the weight on the Moon in comparison to what is
    experienced on Earth = {precent_moon_to_earth} %''')

    precent_moon_to_earth_int = round(precent_moon_to_earth, 0)
    print(f'''The percentage of the weight on the Moon in comparison to what is
    experienced on Earth expressed as an integer = {precent_moon_to_earth_int} %\n''')

mass_calc()