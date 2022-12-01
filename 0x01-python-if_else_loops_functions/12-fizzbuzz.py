#!/usr/bin/python3

def fizzbuzz():
    '''prints the numbers from 1 to 100 separated by a space

       Return: None
    '''
    sep = ' '
    for num in range(1, 101):
        if num % 5 == 0 and num % 3 == 0:
            print("{:s}".format("FizzBuzz"), end=sep)

        elif num % 3 == 0:
            print("{:s}".format("Fizz"), end=sep)

        elif num % 5 == 0:
            print("{:s}".format("Buzz"), end=sep)

        else:
            print("{:d}".format(num), end=sep)
