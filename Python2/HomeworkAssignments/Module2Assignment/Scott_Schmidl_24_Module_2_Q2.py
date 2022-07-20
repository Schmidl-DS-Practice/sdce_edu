# Scott Schmidl - COMP 661 - Programming with Python II - 04/12/2021 to 06/10/2021 - Section 2.4 Module 2 Assignment

from string import ascii_lowercase
import random

def select_random(seq, num):

    '''
    RETURN: RANDOM NUM OF CHARS FROM A SEQUENCE
    ARGUMENTS: SEQ - LIST; NUM - INT
    '''
    return random.choices(population=seq, k=num)

def sort_seq(seq, rev=False):

    '''
    RETURN: A SEQ EITHER REVERSED OR NOT
    ARGUMENTS: SEQ - LIST; REV - BOOL
    '''

    if rev:
        return seq.sort(reverse=rev)
    else:
        return seq.sort()

def get_unique(seq):
    '''
    RETURN: UNIQUE VALUES IN SEQUENCE
    ARGUMENTS: SEQ - LIST
    '''

    return list(set(seq))

def main():

    # DEFINE A LIST OF LOWERCASE LETTERS
    alph = [let for let in ascii_lowercase]
    num_rand = 10

    # GET A NEW RANDOM LIST
    rand_alph = select_random(seq=alph, num=num_rand)
    print(f'Random Letters\n{rand_alph}')

    # SORT DESCENDING
    sort_seq(rand_alph, True)
    print(f'Sort the list in descending order.\n{rand_alph}')

    # SORT ASCENDING
    sort_seq(rand_alph)
    print(f'Sort the list in ascending order.\n{rand_alph}')

    # GET UNIQUE AND SORT ASCENDING
    unique = get_unique(rand_alph)
    sort_seq(unique)
    print(f'Unique values sorted in ascending order.\n{unique}')

if __name__ == '__main__':
    main()