#a program that computes a given integer power of a given number using a for loop.
#Define clearly the input,output and the relations/operations your program is supposed to have. Plan the basic structure of your program then code in python.
# input = integer, exponent
#output = prompt to enter integer, power of the integer

import math

#ask for input from user
value = int(input("Enter the number:"))
exponent = int(input("Enter the exponent:"))

power = 1

for i in range(1, exponent + 1):
    power = power * value

print(value, "^", exponent, "=", power)
