X = input()
Y = input()

n = len(X)
m = len(Y)

lcs = [[0] * (m+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        if X[i-1] == Y[j-1]:
            lcs[i][j] = lcs[i-1][j-1] + 1
        else:
            lcs[i][j] = max(lcs[i][j-1], lcs[i-1][j])

print(lcs)