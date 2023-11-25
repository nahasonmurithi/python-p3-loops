#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i >= 0:
        if i == 0:
            print("Happy New Year!")
        else:
            print (i)
        i -= 1

def square_integers(int_list):
    squaredResult = [num ** 2 for num in int_list]
    return squaredResult

def fizzbuzz():
    num = 1
    while num <= 100:
        if num % 3*5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
      
fizzbuzz()