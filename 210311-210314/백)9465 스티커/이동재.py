import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    sticker = []
    for _ in range(2):
        sticker.append([0, 0] + list(map(int, input().split())))

    dp = [[0 for _ in range(N+2)] for _ in range(2)]
    for i in range(2, N+2):
        dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + sticker[0][i]
        dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + sticker[1][i]
    
    print(max(dp[0][N+1], dp[1][N+1]))
