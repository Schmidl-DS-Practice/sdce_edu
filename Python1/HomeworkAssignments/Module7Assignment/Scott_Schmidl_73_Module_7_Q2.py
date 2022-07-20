#Scott Schmidl - COMP 660 - Programming with Python I - 02/01/2021 to 04/10/2021 - Section 7.3 Module 7 Assignment

#Question 2
num_bytes = int(input('Enter number of Bytes for which you would like to determine the signed range: '))
bits_per_byte = 8
num_bits = num_bytes * bits_per_byte
encode = 2**num_bits
pos_half_encode = encode / 2
neg_half_encode = -pos_half_encode

print('''{0:,} Byte(s) integral type with {1:,} bits can encode {2:,} numbers.
The signed range will be from {3:,.0f} to {4:,.0f}.'''.format(num_bytes, bits_per_byte, encode, neg_half_encode,
                                                pos_half_encode))