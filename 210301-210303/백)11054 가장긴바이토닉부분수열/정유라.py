# http://boj.kr/11054

n = int(input())
s = list(map(int, input().split()))

increase_dp = [1] * n
decrease_dp = [1] * n
for i in range(n):
    for j in range(i):
        if s[i] > s[j]:
            increase_dp[i] = max(increase_dp[i], increase_dp[j]+1)

print(increase_dp)
for i in range(n-1, -1, -1):
    for j in range(i+1, n):
        if s[i] > s[j]:
            decrease_dp[i] = max(decrease_dp[i], decrease_dp[j]+1)

print(decrease_dp)
MAX = 0
for k in range(n):
    if MAX < (increase_dp[k]+decrease_dp[k]):
        MAX = increase_dp[k] + decrease_dp[k]
    

print(MAX-1)