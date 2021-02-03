# 1 -> K -> X
N, M = map(int, input().split())
INF = float('inf')
floyd = [[INF for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
    company1, company2 = map(int, input().split())
    floyd[company1][company2] = 1
    floyd[company2][company1] = 1
X, K = map(int, input().split())

# for row in floyd:
#     for elem in row:
#         print(elem, end="\t")
    # print()

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            floyd[i][j] = min(floyd[i][j], floyd[i][k] + floyd[k][j])

# for row in floyd:
#     for elem in row:
#         print(elem, end="\t")
#     print()

answer = floyd[1][K] + floyd[K][X]
if answer == INF:
    print(-1)
else:
    print(answer)

"""
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5
"""