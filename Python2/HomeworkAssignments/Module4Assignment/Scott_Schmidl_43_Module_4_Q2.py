# Scott Schmidl - COMP 661 - Programming with Python II - 04/12/2021 to 06/10/2021 - Section 4.2 Module 4 Assignment

with open('file.txt', 'r') as test:
    test_file = test.readlines()
    lines = [line.strip() for line in test_file]

count = 0
for line in lines:
    for word in line.split():
        if word.isalpha() and len(word) == 5:
            print(word)
            count += 1
print(count)
