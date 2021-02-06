from pprint import pprint

N, M = map(int, input().split())
INF = float('inf')
floyd = [[INF for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    floyd[A][B] = 1

for i in range(1, N+1):
    floyd[i][i] = 0

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            floyd[i][j] = min(floyd[i][j], floyd[i][k] + floyd[j][k])

# [i][j]와 [j][i]를 둘 다 확인해야 하는 이유를 모르겠음
# 어차피 하나가 INF면 다른 하나도 INF 아닐까 싶은데
answer = N
for row in floyd[1:]:
    know = True
    for dist in row[1:]:
        if dist == INF:
            know = False
            break
    if know == False:
        answer -= 1

print(answer)
