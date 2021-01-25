# 파이썬 내장 라이브러리 중 bisect를 이용한 것
import bisect

N = 5
all_parts = [8, 3, 7, 9, 2]
all_parts.sort()

M = 3
orders = [5,7,9]

def binary_search(arr, x):
    i = bisect.bisect_left(arr, x)
    return i < len(arr) and arr[i] == x

for order in orders:
    if binary_search(all_parts, order):
        print('yes', end=" ")
    else:
        print('no', end=" ")