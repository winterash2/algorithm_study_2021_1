import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[0 for _ in range(N+1)]]
dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
for _ in range(N):
    graph.append([0] + list(map(int, input().split())))

# [print(x) for x in graph]

for i in range(1, N+1):
    sum = 0
    for j in range(1, N+1):
        sum += graph[i][j]
        dp[i][j] = dp[i-1][j] + sum

# [print(x) for x in dp]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    result = dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1]
    print(result)