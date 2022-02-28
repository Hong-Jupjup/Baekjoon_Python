import sys

def binary_serach(arr, target, res):
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
res = [0] * M

for i in ls2:
    result = binary_serach(ls1, i, res)
    if result >= 0 :
        