"""
Aim:    Find the numbers in a list.
Input:  The first line is given N.
        The next line is given N natural numbers.
        The next line is given M.
        The next line is given M natural numbers.
Output: If the number is in the list, print 1, or print 0.
"""
# 함수 내에서 sort를 하니까 시간 초과가 나온다.
# 함수를 부르기 전에 arr을 미리 sort한다.

import sys

def binary_serach(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return -1

N = int(sys.stdin.readline())
ls1 = sorted(list(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline())
ls2 = list(map(int, sys.stdin.readline().split()))

for i in range(M):
    if binary_serach(ls1, ls2[i]) >= 0:
        print(1)
    else:
        print(0)