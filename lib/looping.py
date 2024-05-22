#!/usr/bin/env python3

def happy_new_year():
    counter = 10
    while counter in range(10, 0, -1):
        print(happy_new_year)
        counter -= 1
     # type: ignore
       # code goes here!


def square_integers(int_list):
   square_integers([1, 2, 3, 4, 5])
   return (int_list)*2
    # code goes here!
def fizzbuzz(num):
    for num in range( 1 ,100):
        if not num % 15:
            print("FizzBuzz")
        elif not num % 5:
            print("Buzz")
        elif not num % 3:
            print("Fizz")
        
            