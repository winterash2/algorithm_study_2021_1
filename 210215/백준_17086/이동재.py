from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for i in range(N):
    graph[i] = list(map(int, input().split()))

# [print(graph[i]) for i in range(N)]

def bfs(dp, x, y):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    q = deque()
    q.append((x, y))
    dist = -1
    while q:
        dist += 1
        for _ in range(len(q)):
            x, y = q.popleft()
            if x < 0 or x >= N or y < 0 or y >= M or dist >= dp[x][y]:
                continue
            dp[x][y] = dist
            for d in directions:
                q.append((x + d[0], y + d[1]))

dp = [[1e9 for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            bfs(dp, i, j)

answer = 0
for i in range(N):
    for j in range(M):
        if dp[i][j] > answer:
            answer = dp[i][j]

print(answer)


"""
5 4
0 0 1 0
0 0 0 0
1 0 0 0
0 0 0 0
0 0 0 1
"""