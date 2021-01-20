from itertools import combinations
import copy

N, M = map(int, input().split())
lab_org = []
for _ in range(N):
    lab_org.append(list(map(int, input().split())))

blank = []
for i in range(N):
    for j in range(M):
        if lab_org[i][j] == 0:
            blank.append((i, j))

combi = list(combinations(blank, 3))


def grassfire(lab, x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return
    if lab[x][y] == 0:
        lab[x][y] = 2
        grassfire(lab, x-1, y)
        grassfire(lab, x+1, y)
        grassfire(lab, x, y-1)
        grassfire(lab, x, y+1)
    return


max_count_0 = 0
for com in combi:
    lab = copy.deepcopy(lab_org)
    for c in com:
        lab[c[0]][c[1]] = 1
    for x in range(N):
        for y in range(M):
            if lab[x][y] == 2:
                lab[x][y] = 0
                grassfire(lab, x, y)
    count_0 = 0
    for l in lab:
        count_0 += l.count(0)
    if count_0 > max_count_0:
        max_count_0 = count_0

print(max_count_0)
