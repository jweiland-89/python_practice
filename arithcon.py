#!/usr/bin/env python3

"""Return products and sums"""

def arith():
    while True:
        # User input of 2 numbers
        number_input1 = input("Enter a number: ")
        number_input2 = input("Enter another number: ")
        # Ensure those numbers are integers
        number1 = int(number_input1)
        number2 = int(number_input2)
        # Loop to determine if numbers multiplied are less than or equal to 1000
        if number1 * number2 <= 1000:
            print(number1 * number2)
        else: #print the sum of two numbers if greater than or equal to 1000
            print(number1 + number2)
            continue

arith()
