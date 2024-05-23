#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    count = 10
    while count >= 1:
        print(count)
        count -= 1
    print("Happy New Year!")

happy_new_year()

def square_integers(int_list):
    # code goes here!
    squared_list = [x**2 for x in int_list]
    return squared_list

result = square_integers([1, 2, 3, 4, 5])
print(result)  # Output: [1, 4, 9, 16, 25]
   

def fizzbuzz():
    # code goes here!
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizzbuzz()
