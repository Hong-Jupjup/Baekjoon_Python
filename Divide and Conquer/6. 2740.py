import sys

# Input
row_A, col_A = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(row_A)]
row_B, col_B = map(int, sys.stdin.readline().split())
B = [list(map(int, sys.stdin.readline().split())) for _ in range(row_B)]

# Result Array
C = [[0]*col_B for _ in range(row_A)]

# Multiple Two Arrays
for i in range(row_A):
    for j in range(col_B):
        for k in range(col_A):
            C[i][j] += A[i][k] * B[k][j]

# Output
for i in range(row_A):
    for j in range(col_B):
        print(C[i][j], end = ' ')
    print()