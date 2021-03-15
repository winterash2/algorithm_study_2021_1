import sys
input = sys.stdin.readline

N = int(input())
scores = []
for _ in range(N):
    scores.append(int(input()))

dp1 = [0 for _ in range(N)]
dp2 = [0 for _ in range(N)]

# 0번 칸 초기화
dp1[0] = scores[0]

if N == 1:
    print(scores[0])
else: # N이 2보다 클 때
    # 2번 칸 초기화
    dp1[1] = scores[1]
    dp2[1] = scores[1] + dp1[0]

    for i in range(2, N):
        dp1[i] = scores[i] + max(dp1[i-2], dp2[i-2])
        dp2[i] = scores[i] + dp1[i-1]

    print(max(dp1[N-1], dp2[N-1]))