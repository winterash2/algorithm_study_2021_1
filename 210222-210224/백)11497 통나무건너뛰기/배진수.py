import sys
from collections import deque
input = sys.stdin.readline


testcase = int(input())
for _ in range(testcase):
    n = int(input())
    trees = list(map(int, input().split()))
    trees.sort(reverse=True)

    res = deque()
    res.append(trees[0])
    answer = 0
    for i in range(1,n):
        if i % 2 == 0:
            answer = max(answer, res[0] - trees[i])
            res.appendleft(trees[i])
        else:
            answer = max(answer, res[-1] - trees[i])
            res.append(trees[i])
    answer = max(answer, abs(res[-1] - res[0]))
    # print(res)
    print(answer)
