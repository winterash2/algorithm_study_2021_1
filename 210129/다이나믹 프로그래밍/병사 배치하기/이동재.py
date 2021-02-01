# 이진탐색을 이용한 최장 증가 부분 수열 (LIS : Longest Increasing Subsequence) 구하기
# 책에 있는 방식 916ms, 이 방식 68ms
import bisect
N = int(input())
soldiers = list(map(int, input().split()))
soldiers.reverse()

dp = []
dp.append(soldiers[0])

for soldier in soldiers:
    if soldier > dp[-1]:
        dp.append(soldier)
    else:
        index = bisect.bisect_left(dp, soldier)
        dp[index] = soldier
print(N-len(dp))

"""
N = int(input())
soldiers = list(map(int, input().split()))

# N = 7
# soldiers = [15, 11, 4, 8, 5, 2, 4]

dp = [1] * N  # 여기서 초기화를 0으로 래서 틀렸었음
dp[0] = 1
print(dp)

for i in range(1, N, 1):
    for j in range(i):
        if soldiers[j] > soldiers[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(N - max(dp))
"""

