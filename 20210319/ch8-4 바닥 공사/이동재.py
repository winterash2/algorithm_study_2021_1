N = int(input())
dp = [0 for _ in range(1001)]
dp[0] = 0
dp[1] = 1
dp[2] = 3
for i in range(3, N+1):
    dp[i] += dp[i-2] * 2
    dp[i] += dp[i-1]
    dp[i] = dp[i] % 796796
print(dp[N])
