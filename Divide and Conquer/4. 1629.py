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