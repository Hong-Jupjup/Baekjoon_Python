"""
Aim:    Similar to a quadtree, but divide it into 9 instead of 4.
Input:  The first line is given N(1<=N<=3^7, N is 3^k).
        The next N lines are given N integers.
Output: The numbers of papers filled with only -1, 0 and 1.
"""

import sys

# Input
n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# Result
result1 = 0
result2 = 0
result3 = 0

# Divide and Check
def divide(x, y, n):
    global result1, result2, result3
    check = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if check != arr[i][j]:
                divide(x, y, n//3)
                divide(x, y+n//3, n//3)
                divide(x, y+n//3*2, n//3)
                divide(x+n//3, y, n//3)
                divide(x+n//3, y+n//3, n//3)
                divide(x+n//3, y+n//3*2, n//3)
                divide(x+n//3*2, y, n//3)
                divide(x+n//3*2, y+n//3, n//3)
                divide(x+n//3*2, y+n//3*2, n//3)
                return

    if check==-1:
        result1 += 1
    elif check==0:
        result2 += 1
    else:
        result3 += 1

divide(0, 0, n)
print(result1)
print(result2)
print(result3)