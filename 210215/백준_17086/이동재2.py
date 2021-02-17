from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for i in range(N):
    graph[i] = list(map(int, input().split()))

# [print(graph[i]) for i in range(N)]

def bfs(dp, q, x, y):
    dist = 0
    while q:
        for _ in range(len(q)):
            x, y = q.popleft()
            if x < 0 or x >= N or y < 0 or y >= M or dp[x][y] != 1e9 or dist >= dp[x][y]:
                continue
            dp[x][y] = dist
            for d in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                q.append((x + d[0], y + d[1]))
        dist += 1

dp = [[1e9 for _ in range(M)] for _ in range(N)]
q = deque()
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            q.append((i, j))

bfs(dp, q, i, j)

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