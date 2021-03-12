# 1차 시도. 벽을 하나씩 없애고 전부 다시 구하는 방식
# 시간초과됨
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append([int(x) for x in input().split()[0]])


def calc(graph):
    dp = [[0 for _ in range(M)] for _ in range(N)]
    q = deque()
    q.append((0, 0))
    depth = 0
    while q:
        depth += 1
        for _ in range(len(q)):
            x, y = q.popleft()
            if x < 0 or x >= N or y < 0 or y >= M:
                continue
            if dp[x][y] != 0 or graph[x][y] == 1:
                continue
            # print(x, y)
            dp[x][y] = depth
            q.append((x-1, y))
            q.append((x+1, y))
            q.append((x, y-1))
            q.append((x, y+1))

    if dp[N-1][M-1] == 0:
        return 1e9
    else:
        return dp[N-1][M-1]


answer = 1e9
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            graph[i][j] = 0
            answer = min(answer, calc(graph))
            graph[i][j] = 1

if answer == 1e9:
    print(-1)
else:
    print(answer)
