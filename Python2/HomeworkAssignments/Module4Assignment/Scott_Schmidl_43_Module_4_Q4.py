# Scott Schmidl - COMP 661 - Programming with Python II - 04/12/2021 to 06/10/2021 - Section 4.2 Module 4 Assignment

while True:

    file_path = input('Enter the file name: ')

    try:
        with open(file_path) as here:
            here_file = here.readlines()
            lines = [line.strip() for line in here_file]
            print(lines)
            break

    except:
        print('This file does not exist.\n')