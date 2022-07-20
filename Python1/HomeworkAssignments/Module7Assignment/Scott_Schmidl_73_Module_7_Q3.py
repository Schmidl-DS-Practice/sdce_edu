#Scott Schmidl - COMP 660 - Programming with Python I - 02/01/2021 to 04/10/2021 - Section 7.3 Module 7 Assignment

#Question 3

#ideal gas constant in (kg * m**2 / sec**2) / K * mol
R = 8.3145

#absolute temperature in Kelvin
celsius = int(input('Enter a temperature in Celsius: '))
T = celsius + 273

#mass of a mole of the gas in kilograms. molar mass of O**2(oxygen) in kg/mol
M = 3.2 * 10**-2

#root mean square velocity in meters/second
rms_velocity = ((3 * R * T) / M)**0.5


print('''The average velocity or root mean square velocity of a molecule in a sample of oxygen
at {0:,} degrees Celsius is {1:,.3f} m/sec'''.format(celsius, rms_velocity))
