#!/usr/bin/env python
# HW03_ex06
# (1) Please comment your code.
# (2) Please be thoughtful when naming your variables.
# (3) Please remove development code before submitting.
################################################################################
# Exercise 1
# When you submit only include your final function: compare

def compare(x, y):
    if x > y :
        temp = 1
        print ("x is greater than y")
        return temp
    elif x == y : 
        temp = 0
        print("x and y are equal")
        return temp
    else : 
        temp = -1
        print("x is less than y")
        return temp 



################################################################################
# Exercise 2
# When you submit only include your final function: hypotenuse
# Do develop incrementally. Do not share here.

import math

def hypotenuse(a, b):
    cSquared = a**2 + b**2
    c = math.sqrt(cSquared)
    print (c)




################################################################################
# Exercise 3
# When you submit only include your final function: is_between

def is_between(x, y, z):
    if x <= y & y <=z:
        print("True")
        return True
    else:
        print("False")
        return False



################################################################################
# Exercise 6
# When you submit only include your final function: is_palindrome


def first(word):
    return word[0]
def last(word):
    return word[-1]
def middle(word):
    return word[1:-1]

def is_palindrome(word):
    backward = word[::-1]
    if first(word) == last(word) and middle(word) == middle(backward) :
        return True
    else :
        return False


################################################################################
# Exercise 7
# When you submit only include your final function: is_power

def is_power(a, b):
    c = a / b  
    if a%b != 0 or c%b != 0:
        return False
    else :
        return True



################################################################################
def main():
    """Your functions will be called within this function."""
    ############################################################################
    # Use this space temporarily to call functions in development:
    print("Hello World!")







    ############################################################################
    # Uncomment the below to test and before commiting:
    # # Exercise 1
    compare(1,1)
    compare(1,2)
    compare(2,1)
    # # Exercise 2
    hypotenuse(1,1)
    hypotenuse(3,4)
    hypotenuse(1.2,12)
    # # Exercise 3
    is_between(1,2,3)
    is_between(2,1,3)
    is_between(3,1,2)
    is_between(1,1,2)

    # # Exercise 6
    print is_palindrome("Python")
    print is_palindrome("evitative")
    print is_palindrome("sememes")
    print is_palindrome("oooooooooooo")
    # # Exercise 7
    print is_power(28,3)
    print is_power(27,3)
    print is_power(248832,12)
    print is_power(248844,12)


if __name__ == "__main__":
    main()