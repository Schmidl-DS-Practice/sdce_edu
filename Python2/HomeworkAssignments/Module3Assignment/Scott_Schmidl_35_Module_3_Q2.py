# Scott Schmidl - COMP 661 - Programming with Python II - 04/12/2021 to 06/10/2021 - Section 3.5 Module 3 Assignment

from collections import Counter

text = '''Peter Piper picked a peck of pickled peppers A peck of pickled peppers Peter Piper picked \
if Peter Piper picked a peck of pickled peppers Where is the peck of pickled peppers Peter Piper picked'''

words = text.lower().split(' ')
words.sort()

count_words = Counter(words)

print('WORD        COUNT')
for word, count in count_words.items():
    if count > 1:
        print(f'{word:<7}{count:>8d}')