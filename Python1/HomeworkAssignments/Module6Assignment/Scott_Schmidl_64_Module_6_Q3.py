#Scott Schmidl - COMP 660 - Programming with Python I - 02/01/2021 to 04/10/2021 - Section 6.4 Module 6 Assignment

#Question 3
def count_address(s, counts):

    '''
    loop through a string, count the number of internet addresses
    by using the split method.
    s -> string
    '''

    #THIS COUNTS WHAT'S IN THE ()
    u = s.count(counts)

    #ACCUMULATOR FOR HOW MANY INTERNET ADDRESS
    address = len(s.split('\n'))
    # counter = 0
    # for _ in s.split('\n'):
    #     counter += 1
    return address, u

s = '''inet addr :127.0.0.1 Mask:255.0.0.0
        inet addr :127.0.0.2 Mask:255.0.0.0
        inet addr :127.0.0.3 Mask:255.0.0.0
        inet addr :127.0.0.4 Mask:255.0.0.0'''
counts = 'inet addr'

# Question3A, Question3B = count_address(s, counts)
# print(f'Count of Internet Addresss: {Question3A}', f'\nCount of "inet addr" in the string: {Question3B}')

chunk = s.split('\n')
counter = 0
for address in chunk:
    if 'inet addr' in address:
        counter += 1
print(counter)
