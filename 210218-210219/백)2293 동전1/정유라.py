# http://boj.kr/2293
# dp 문제

n, k = map(int, input().split())
dp = [0] * (k+1)
dp[0] = 1
coins = []
for _ in range(n):
    coin = int(input())
    coins.append(coin)

for coin in coins:
    for j in range(coin, k+1):
        dp[j] += dp[j-coin]
print(dp)
print(dp[k])