# Scott Schmidl - COMP 661 - Programming with Python II - 04/12/2021 to 06/10/2021 - Section 3.5 Module 3 Assignment

temperatures = {'Monday': [67, 71, 74, 77],
                'Tuesday': [52, 56, 66 , 50],
                'Wednesday': [77, 80, 87 , 95],
                'Thursday': [67, 77, 81 , 77],
                'Friday': [54 , 60 , 67, 60]}

for k, v in temperatures.items():
    print(f'{k}: {sum(v)/len(v):.0f}')

'''
THIS FOR LOOP PRINTS THE DAY OF THE WEEK AND THE MEAN OF ITS TEMPTERATURES.
'''