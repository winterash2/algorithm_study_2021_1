N, M = map(int, input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))

coins.sort(reverse=True)
INF = float('inf')
dp = [INF] * (M+1)
dp[0] = 0
for coin in coins:
    for i in range(coin, M+1):
        dp[i] = min(dp[i], dp[i-coin] + 1)

if dp[M] == INF:
    print(-1)
else:
    print(dp[M])