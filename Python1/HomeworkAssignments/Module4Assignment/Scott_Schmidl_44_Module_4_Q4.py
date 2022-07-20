#Scott Schmidl - COMP 660 - Programming with Python I - 02/01/2021 to 04/10/2021 - Section 4.4 Module 4 Assignment

#Question 4
import math

def velocity_final(d, u=0, a=9.8 ):
    final_velocity = u**2 + (2*a*d)
    return round(math.sqrt(final_velocity), 1)

def main():
    final_velocity = velocity_final(51)
    return f'final velocity: {final_velocity} meters/second'

if __name__ == '__main__':
    print('\ncalling expression with u and a as defaults: final_velocity = velocity_final(51)')
    print(main())