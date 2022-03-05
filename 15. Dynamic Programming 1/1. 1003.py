"""
Aim:    When calling fibonacci(N), how many times 0 and 1 are printed, respectively.
Input:  The first line is given T(test case).
        The next line is given N, which is a natural number less than 40 or 0.
Output: For each test cases, print the number of 0 printed and 1 .
"""

import sys
t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    zero = 1
    one = 0
    tmp = 0
    for _ in range(n):
        tmp = one
        one = one + zero
        zero = tmp
    print(zero, one)