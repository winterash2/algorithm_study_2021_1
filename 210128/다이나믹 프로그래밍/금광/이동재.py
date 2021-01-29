from collections import deque
T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    mine = [[0 for _ in range(M)] for _ in range(N) ]
    dp = [[0 for _ in range(M)] for _ in range(N) ]
    data = list(map(int, input().split()))
    for i in range(N):
        for j in range(M):
            mine[i][j] = data[i*M+j]

    for i in range(N):
        dp[i][0] = mine[i][0]

    for j in range(M-1):
        for i in range(N):
            if i-1 >= 0:
                # 오른쪽 위
                dp[i-1][j+1] = max(dp[i-1][j+1], dp[i][j] + mine[i-1][j+1])
            if i+1 < N:
                # 오른쪽 아래
                dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + mine[i+1][j+1])
            # 오른쪽
            dp[i][j+1] = max(dp[i][j+1], dp[i][j] + mine[i][j+1])

    max_val = 0
    for i in range(N):
        max_val = max(max_val, dp[i][M-1])
    print(max_val)