# Scott Schmidl - COMP 661 - Programming with Python II - 04/12/2021 to 06/10/2021 - Section 2.4 Module 2 Assignment

def sorting(lst):

    '''
    RETURN: A REVERSED SORTED LIST USING THE SORT METHOD
    ARGUMENT: LIST - LIST()
    '''

    return lst.sort(reverse=True)

def main():

    # DEFINE TWO LIST
    list_num = [81, 12, 323, 44, 105, 63, 17, 8, 92]
    list_let = ['d', 'b', 'c', 'a', 'h', 'g', 'i', 'f', 'w' ]

    # SORTING LIST OF NUMBERS IN REVERSE ORDER TO ANSWER THE QUESTION
    sorting(list_num)
    print(list_num)

    # SORTING LIST OF LOWERCASE LETTERS IN REVERSE ORDER TO ANSWER THE QUESTION
    sorting(list_let)
    print(list_let)

    # PRINT QUESTION WITH THE WORD "REVERSE" FILLED IN TO ANSWER
    print('''Q1. To sort a list in descending order,
    call list method sort with the optional keyword argument REVERSE set to True.''')

if __name__ == '__main__':
    main()