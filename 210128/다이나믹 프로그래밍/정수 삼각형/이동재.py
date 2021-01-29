N = int(input())
tree = []
for _ in range(N):
    tree.append(list(map(int, input().split())))

# N = 5
# tree = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

dp = [[0 for _ in range(len(x))] for x in tree]
dp[0][0] = tree[0][0]

for i in range(len(tree)-1):
    t = tree[i]
    for j in range(len(t)):
        dp[i+1][j] = max(dp[i+1][j], dp[i][j] + tree[i+1][j])
        dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + tree[i+1][j+1])

max_val = 0
for val in dp[N-1]:
    max_val = max(max_val, val)
print(max_val)