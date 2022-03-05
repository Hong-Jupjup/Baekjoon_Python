"""
Condition:
    if a <= 0 or b <= 0 or c <= 0, then w(a, b, c) returns:
        1

    if a > 20 or b > 20 or c > 20, then w(a, b, c) returns:
        w(20, 20, 20)

    if a < b and b < c, then w(a, b, c) returns:
        w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)

    otherwise it returns:
        w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
Input:  a, b and c are given. When a, b and c are all -1, the program is terminated.
Output: Print w(a, b, c)
"""

import sys

def w(a, b, c):
    if a<=0 or b<=0 or c<=0:
        return 1
    
    if a>20 or b>20 or c>20:
        return w(20, 20, 20)
    
    if result[a][b][c]:
        return result[a][b][c]
    
    if a<b<c:
        result[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return result[a][b][c]

    result[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return result[a][b][c]

result = [[[0]*21 for _ in range(21)] for _ in range(21)]

while 1:
    a, b, c = map(int, sys.stdin.readline().split())
    
    if (a, b, c) == (-1, -1, -1):
        break
    
    print('w(%d, %d, %d) = %d' % (a, b, c, w(a, b, c)))