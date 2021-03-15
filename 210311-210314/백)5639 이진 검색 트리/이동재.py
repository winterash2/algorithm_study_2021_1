# 2차로 한 것에 이진탐색을 접목시킴
# 성공. 812ms
# 진수꺼 설명 듣기
from collections import deque
from bisect import bisect_left
import sys
input = sys.stdin.readline

arr = []
while True:
    try:
        arr.append(int(input()))
    except:
        break

answer = []
q = deque()
q.append(arr)
while q:
    arr = q.popleft()
    if len(arr) <= 1:
        answer = answer + arr
        continue
    root = arr[0]
    arr = arr[1:]
    idx = bisect_left(arr, root)
    left = arr[:idx]
    right = arr[idx:]

    q.appendleft([root])
    q.appendleft(right)
    q.appendleft(left)

[print(x) for x in answer]

# 2차 deque로 푼 것
# 이것도 시간 초과 뜸
"""
from collections import deque
import sys
input = sys.stdin.readline

arr = []
while True:
    try:
        arr.append(int(input()))
    except:
        break

answer = []
q = deque()
q.append(arr)
while q:
    arr = q.popleft()
    if len(arr) <= 1:
        answer = answer + arr
        continue
    root = arr[0]
    left = []
    right = []
    for elem in arr[1:]:
        if elem < root:
            left.append(elem)
        else:
            right.append(elem)
    q.appendleft([root])
    q.appendleft(right)
    q.appendleft(left)

[print(x) for x in answer]
"""

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