import sys

# Input
n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# Result
white = 0
blue = 0

# Divide and Check
def divide(x, y, n):
    global white, blue
    check = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if check != arr[i][j]:
                divide(x, y, n//2)
                divide(x, y+n//2, n//2)
                divide(x+n//2, y, n//2)
                divide(x+n//2, y+n//2, n//2)
                return

    if check==0:
        white += 1
    else:
        blue += 1

divide(0, 0, n)
print(white)
print(blue)