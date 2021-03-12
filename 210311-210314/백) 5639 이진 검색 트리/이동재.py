from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)


arr = []
while True:
    try:
        arr.append(int(input()))
    except:
        break


def loop(arr):
    if len(arr) <= 1:
        return arr
    # 리스트일 때
    root = arr[0]
    left = []
    right = []
    for elem in arr[1:]:
        if elem < root:
            left.append(elem)
        else:
            right.append(elem)

    left = loop(left)
    right = loop(right)
    return left + right + [root]


answer = loop(arr)
[print(x) for x in answer]

# 1차 recursion으로 푼 것
# 시간 초과 됨
"""
from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)


arr = []
while True:
    try:
        arr.append(int(input()))
    except:
        break


def loop(arr):
    if len(arr) <= 1:
        return arr
    # 리스트일 때
    root = arr[0]
    left = []
    right = []
    for elem in arr[1:]:
        if elem < root:
            left.append(elem)
        else:
            right.append(elem)

    left = loop(left)
    right = loop(right)
    return left + right + [root]


answer = loop(arr)
[print(x) for x in answer]

"""