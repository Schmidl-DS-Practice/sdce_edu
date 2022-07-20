#Scott Schmidl - COMP 660 - Programming with Python I - 02/01/2021 to 04/10/2021 - Section 4.4 Module 4 Assignment

#Question 5
from Scott_Schmidl_44_Module_4_Q4 import velocity_final

def elapsed_time(v, u, a=9.8):
    '''final velocity = initial velocity + acceleration * elapsed_time
    rearrange the equation to find time'''
    time = (v - u) / a
    return round(time, 1)

final_velocity = velocity_final(51)
time_elapsed = elapsed_time(final_velocity, 0)
print(f'time elapsed: {time_elapsed} seconds')