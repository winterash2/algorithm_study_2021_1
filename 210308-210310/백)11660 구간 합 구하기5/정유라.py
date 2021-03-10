# 가로만 더했는데 시간초과남
# 세로축도 포함해서 더해야함
# 다시풀어보기
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

res = 0
arr = []
for _ in range(n):
    input_list = list(map(int, input().split()))
    arr.append(input_list)

dp = [[0] * (n) for _ in range(n)]

for i in range(n):
    temp = 0
    for j in range(n):
        dp[i][j] = arr[i][j] + temp
        temp = dp[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    answer = 0
    for i in range(x1-1, x2):
        answer += dp[i][y2 - 1]
        if y1 > 1:
            answer -= dp[i][y1 - 2]
    print(answer)
