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