import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []

shark = 0
for i in range(n):
    temp = list(map(int, input().split()))
    for t in temp:
        if t == 1:
            shark += 1
    arr.append(temp)

mx = [-1, -1, -1, 0, 1, 0, 1, 1]
my = [-1, 0, 1, 1, 1, -1, 0, -1]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    dist = 0
    while q:
        dist += 1
        for _ in range(len(q)):
            x, y = q.popleft()
            for k in range(8):
                dx = x + mx[k]
                dy = y + my[k]
                if 0 <= dx < n and 0 <= dy < m:
                    if arr[dx][dy] == 1:
                        return dist
                    else:
                        q.append((dx, dy))
    return

safe_dist = 0
if shark == 0:
    print(0)
else:
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                res = bfs(i,j)
                safe_dist = max(safe_dist, res)
    print(safe_dist)