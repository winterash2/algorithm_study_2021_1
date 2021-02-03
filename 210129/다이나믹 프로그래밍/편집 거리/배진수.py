INF = int(1e9)

A = input()
B = input()

dp = [[INF for _ in range(len(B)+1)] for _ in range(len(A)+1)]
dp[0][0] = 0

for i in range(len(B)):
    dp[0][i+1] = ord(B[i])

for i in range(len(A)):
    dp[i+1][0] = ord(A[i])

for i in range(1, len(A) + 1):
    for j in range(1, len(B) + 1):
        if dp[0][j] == dp[i][0]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1

print(dp[-1][-1])
for i in range(len(A)+1):
    for j in range(1, len(B) + 1):
        print(dp[i][j], end= "")
    print()
