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
# 어차피 하나가 INF면 다른 하나도 INF 아닐까 싶은데 -> 내가 코드를 잘 못 짰음
# L16 보면 [i][k] + [j][k] 로 해놨음, 원래 [i][k] + [k][j] 인데
# 근데 이렇게 돌려도 문제 없을 것 같음. 그 이유는 ik, jk를 더해서 무한이 아니라는 의미는 k를 사이에 두고 둘 사이의 우위 비교가 된다는 의미이기 때문임
# 따라서 단순히 순위 비교가 가능한지 확인할 때는 이렇게 구현해도 괜찮은 것 같음
answer = N
for row in floyd[1:]:
    know = True
    for dist in row[1:]:
        if dist == INF:
            know = False
            break
    if know == False:
        answer -= 1

pprint(floyd)
pprint(answer)

"""
6 6
1 5
3 4
4 2
4 6
5 2
5 4
"""