#Scott Schmidl - COMP 660 - Programming with Python I - 02/01/2021 to 04/10/2021 - Section 4.4 Module 4 Assignment

#Question 3
def name():
    print("- Albert Einstein")
def quote():
    print("Imagination is more important than ", end="")
def ofthe():
    print("For knowledge is limited, ", end="")
def day():
    print("knowledge. " , end="")
def famous():
    print("stimulating progress, giving birth to evolution ", end="")
def influencers():
    print("whereas imagination embraces the entire world, ", end="")

quote()
day()
ofthe()
influencers()
famous()
name()

output = '''Imagination is more important than knowledge. For knowledge is limited,
whereas imagination embraces the entire world, timulating progress, giving birth to evolution - Albert Einstein'''

output_explanation = '''Even though the functions are defined in a specific order they are called in an order
that allows for the print statements to make sense. The end="" in the 2nd through 6th functions tells the
print statements to place the next sequence of characters on the same line. This leads to a nice couple
sentences.'''

print(f'\noutput explanation: {output_explanation}')