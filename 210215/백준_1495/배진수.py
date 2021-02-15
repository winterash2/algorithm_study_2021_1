# 기타리스트
import sys
input = sys.stdin.readline

"""
def bfs(start, num):
    global n, result, max_v
    if num == n:
        print(start)
        result = max(result, start)
        return
    else:
        if start -v[num] < 0 and start + v[num] > max_v:
            result = max(result, -1)
            return

        if start + v[num] <= max_v:
            start += v[num]
            num += 1
            bfs(start, num)
            num -= 1
            start -= v[num]
        if start - v[num] >= 0:
            start -= v[num]
            num += 1
            bfs(start, num)
            num -= 1
            start += v[num]
    
n, start, max_v = map(int, input().split())
v = list(map(int, input().split()))

result = int(-1e9)
bfs(start, 0)
print(result)
"""

n, start, max_v = map(int, input().split())
v = list(map(int, input().split()))

dp = []
for _ in range(n+1):
    dp_arr = [False] * (max_v + 1)
    dp.append(dp_arr)
dp[0][start] = True

for i in range(n):
    for j in range(max_v+1):
        check = dp[i][j]
        if check:
            if j + v[i] <= max_v:
                dp[i+1][j+v[i]] = True
            if j - v[i] >= 0:
                dp[i+1][j-v[i]] = True

result = -1
for i in range(max_v+1):
    if dp[n][i]:
        result = i
print(result)
