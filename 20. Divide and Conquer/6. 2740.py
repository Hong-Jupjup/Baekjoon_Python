"""
Aim:    Multiplication of matrix.
Input:  The first line is given the size N and M of the matrix A.
        From the second line, M elements of matrix A are given in order in N lines.
        The next line is given the size M and K of the matrix B.
        Subsequently, K elements of matrix B are given in sequence in M rows.
Output: A matrix multiplied by a matrix A and B in N lines.
"""

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