# http://boj.kr/2579
from collections import deque
n = int(input())
stairs = []
dp = []
q = deque()
for _ in range(n):
    stairs.append((int(input()), 0))
    dp.append((0,0))

# 1. 1칸 움직임 -> 2칸 움직여야함
# 2. 2칸 움직임 -> 1칸 or 2칸 가능

# dp배열 안에 (value, 몇칸움직여왔는지 저장)
# 1이면 dp[i+2] = dp[i] + stairs[i+2]
# dp[i]의 값이(value, 2)면 1칸: dp[i+1] = max(dp[i+1], dp[i]+stairs[i+1])
#                         2칸: dp[i+2] = max(dp[i+2], dp[])
# 마지막껄 밟는지 확인하기 위해 큐 사용

dp[0] = (stairs[0][0], 2)

q.append(dp[0])
max_value = -int(1e9)
i = 0
while q:
    print("-----")
    print(q)
    value, step = q.popleft()
    if i+2 >= n:
        continue
    value_1, step_1 = dp[i+1]
    value_2, step_2 = dp[i+2]
    print("value1", value_1, "step1:", step_1)
    print("stairs 2칸뒤", stairs[i+2][0])
    dp[i+2] = (max(value_2, value + stairs[i+2][0]), 2)
    q.append(dp[i+2])
    if i+2 == n-1:
        max_value = max(max_value, dp[i+2][0])
    if step == 2:
        dp[i+1] = (max(value_1, value + stairs[i+1][0]), 1)
        q.append(dp[i+1])
        if i+1 == n-1:
            max_value = max(max_value, dp[i+1][0])
    i+= 1


# for i in range(n):
#     now, cnt = dp[i]
#     if i+2 >= n or i+1 >= n:
#         continue

#     step_1, cnt_1 = dp[i+1]
#     step_2, cnt_2 = dp[i+2]
#     dp[i+2] = (max(step_2, now + stairs[i][0]), 2)
#     if cnt == 2:
#         dp[i+1] = (max(step_1, now + stairs[i+1][0]), 1)
    
print(max_value)