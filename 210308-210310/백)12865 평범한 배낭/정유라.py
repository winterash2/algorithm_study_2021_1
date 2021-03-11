# http://boj.kr/12865
# value기반 dp 뒤에서부터 계산
from collections import deque

n, m = map(int, input().split())
info = []
for _ in range(n):
    w, v = map(int, input().split())
    info.append((w, v))
info.sort()
q = deque(info)
max_value = -int(1e9)

dp = [[0] * (m+1) for _ in range(n+1)]
print(dp)
print(max_value)

# dp[i - 1][j]와 v[i] + dp[i - 1][j - w[i]]중 큰 값을 넣으면 된다.
# 가로: 무게 

for i in range(1, m+1):
    for j in range(1, n+1):
        dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]])