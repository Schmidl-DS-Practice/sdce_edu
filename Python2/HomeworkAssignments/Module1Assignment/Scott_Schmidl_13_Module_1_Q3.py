# Scott Schmidl - COMP 661 - Programming with Python II - 04/12/2021 to 06/10/2021 - Section 1.3 Module 1 Assignment

#from timeit import default_timer as timer

import time

def time_cost(problemSize):

    #Start the algorithm
    work = 1
    for _ in range(problemSize):
        work += 5
        work -= 5
    #end of algorithm

def main():

    #GET HOW MANY NUMBERS TO CHECK
    check = int(input('Enter how many times to count: '))
    #GET SPECIFIC NUMBERS TO CHECK
    problem_size = [int(input('Enter to what number to count: ')) for _ in range(check)]

    #LOOP THROUGH PROBLEM_SIZE AND GET TIME TO RUN FUNCTION
    print('\nProblem Size         Seconds')
    for size in problem_size:
        #START THE TIMER
        #start = timer()
        start = time.time()
        time_cost(size)

        #STOP THE TIMER
        #end = timer()
        end = time.time()

        total_time = round(end - start, 4)

        print(f'{size}              {total_time}\n')

if __name__ == '__main__':
    main()