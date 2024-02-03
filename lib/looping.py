#!/usr/bin/env python3

'''
Write a function happy_new_year() using a while loop that outputs numbers starting at 10 and counting down to 1. 
After reaching 1, print out "Happy New Year!"
'''
def happy_new_year():
    countdown = 10
    while countdown > 0:
        print(countdown)
        countdown -= 1
    print("Happy New Year!")
happy_new_year()

'''
Write a function square_integers() that takes one argument. 
A list of integers and returns the list of squared elements.
'''   
def square_integers(int_list):
    squared_list = [x**2 for x in int_list]
    return squared_list

my_list = [1, 2, 3, 4, 5]
squared_list = square_integers(my_list)
print(squared_list)

'''
Write a function fizzbuzz() that prints the numbers from 1 to 100. 
For multiples of three, print "Fizz" instead of the number and for the multiples of five print "Buzz". 
For numbers which are multiples of both three and five, print "FizzBuzz".
'''
def fizzbuzz():
    number = 1
    while number <= 100:  
        if (number % 3 == 0) and (number % 5 == 0):
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)
        number += 1
fizzbuzz()

