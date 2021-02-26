import sys
input = sys.stdin.readline

N = int(input())
houses = []
for _ in range(N):
    houses.append(list(map(int, input().split())))

dp = [[0, 0, 0] for _ in range(N)]
dp[0] = houses[0]

for i in range(1, N):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + houses[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + houses[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + houses[i][2]

print(min(dp[N-1]))