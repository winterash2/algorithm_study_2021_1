N = int(input())
warehouses = list(map(int, input().split()))

dp = [0 for _ in range(N)]
dp[0] = warehouses[0]
dp[1] = max(dp[0], warehouses[1])
for i in range(2, N):
    dp[i] = max(dp[i-2] + warehouses[i], dp[i-1])
    print(dp)
print(dp[N-1])