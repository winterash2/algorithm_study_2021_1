# 상담원한테 비서가 있는 클라스...
import sys
input = sys.stdin.readline

N = int(input())
sangdams = []
for _ in range(N):
    T, P = map(int, input().split())
    sangdams.append((T, P))

# N = 7
# sangdams = [(3, 10), (5, 20), (1, 10), (1, 20), (2, 15), (4, 40), (2, 200)]
# N = 10
# sangdams = [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5),
#             (1, 6), (1, 7), (1, 8), (1, 9), (1, 10)]
# N = 10
# sangdams = [(5, 50), (4, 40), (3, 30), (2, 20), (1, 10), (1, 10), (2, 20), (3, 30), (4, 40), (5, 50)]

dp = [0 for _ in range(len(sangdams)+1)]
for i in range(N):
    if i != 0:
        dp[i] = max(dp[i-1], dp[i])
    (T, P) = sangdams[i]
    if i+T < N+1:
        dp[i+T] = max(dp[i+T], dp[i]+P)
    # print(dp)

print(max(dp))
