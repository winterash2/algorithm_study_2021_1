# http://boj.kr/2579

n = int(input())
stairs = []
for _ in range(n):
    stairs.append(int(input()))

# 1. 1칸 움직임 -> 2칸 움직여야함
# 2. 2칸 움직임 -> 1칸 or 2칸 가능

# dp배열 안에 (value, 몇칸움직여왔는지 저장)
# 1이면 dp[i+2] = dp[i] + stairs[i+2]
# dp[i]의 값이(value, 2)면 1칸: dp[i+1] = max(dp[i+1], dp[i]+stairs[i+1])
#                         2칸: dp[i+2] = max(dp[i+2], dp[])               