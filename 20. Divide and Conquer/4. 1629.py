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
def divide(tmp, a, b):
    if b==1:
        print(tmp)
        return
    divide((tmp*a)%c, a, b-1)

divide(a, a, b)