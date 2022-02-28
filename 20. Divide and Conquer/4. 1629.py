"""
Aim:    Calculate the power fast using divide and conquer.
Input:  A, B and C are given.
        They are all natural numbers of 2,147,483,647 or less.
Output: The remainder of A multiplied by B times divided by C.
"""

import sys

# Input
a, b, c = map(int, sys.stdin.readline().split())

# Divide and Calculate
def divide(a, b):
    if b == 1:
        return a%c
    else:
        tmp = divide(a, b//2)
        if b%2 == 0:
            return (tmp*tmp)%c
        else:
            return (tmp*tmp*a)%c

print(divide(a, b))