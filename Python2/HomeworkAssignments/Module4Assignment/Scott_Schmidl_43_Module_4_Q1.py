# Scott Schmidl - COMP 661 - Programming with Python II - 04/12/2021 to 06/10/2021 - Section 4.2 Module 4 Assignment

with open('file.txt', 'r') as test:
    test_file = test.readlines()
    count = 0
    for line in test_file:
        count +=1
        print(line.strip())
    print(f'Number of lines in the file: {count}')
