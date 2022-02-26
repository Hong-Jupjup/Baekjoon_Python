import sys

# Input
n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]

# Divide and Check
def divide(x, y, n):
    check = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if check != arr[i][j]:
                print('(', end='')
                divide(x, y, n//2)
                divide(x, y+n//2, n//2)
                divide(x+n//2, y, n//2)
                divide(x+n//2, y+n//2, n//2)
                print(')', end='')
                return

    if check==0:
        print('0', end='')
    else:
        print('1', end='')

divide(0, 0, n)
print()