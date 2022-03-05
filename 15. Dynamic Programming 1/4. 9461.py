"""
Aim:    Padovan sequence: 1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12, ...
Input:  The first line is given T(test case).
        The next T lines are given N(1 <= N <= 100).
Output: Print P(N) for each test case.
"""

import sys
t = int(sys.stdin.readline())

ls = [1, 1, 1, 2, 2]
for i in range(5, 100):
    ls.append(ls[i-1] + ls[i-5])

for _ in range(t):
    n = int(sys.stdin.readline())
    print(ls[n-1])