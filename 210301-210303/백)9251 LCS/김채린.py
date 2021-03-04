# https://www.acmicpc.net/problem/9251

m = list(input())
n = list(input())
m_len = len(m)
n_len = len(n)


a = [[0] * (n_len + 1) for i in range(m_len + 1)]
for i in range(m_len):
    for j in range(n_len):
        if m[i] == n[j]:
            a[i + 1][j + 1] = a[i][j] + 1
        else:
            a[i + 1][j + 1] = max(a[i][j + 1], a[i + 1][j])
print(a[m_len][n_len])