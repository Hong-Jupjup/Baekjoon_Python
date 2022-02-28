"""
Aim:    Find all the sequences that have numbers from 1 to N without overlapping.
Input:  N and M.
Output: Sequences that are sorted in ascending order and meet the conditions.
"""

import sys

def dfs():
    if len(s) == m:
#        print(' '.join(map(str, s)))
        return

    for i in range(1, n+1):
        if i in s:
            continue
        s.append(i)
        print(s)
        dfs()
        s.pop()

n, m = map(int, sys.stdin.readline().split())
s = []

dfs()