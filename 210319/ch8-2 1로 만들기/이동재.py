X = int(input())
INF = float('inf')
dp = [INF for _ in range(X+1)]
dp[1] = 1
for i in range(X):
    if dp[i] != 0:
        if i * 2 <= X:
            dp[i*2] = min(dp[i]+1, dp[i*2])
        if i * 3 <= X:
            dp[i*3] = min(dp[i]+1, dp[i*3])
        if i * 5 <= X:
            dp[i*5] = min(dp[i]+1, dp[i*5])
        dp[i+1] = min(dp[i+1], dp[i]+1)

print(dp[X]-1)