# N, M = [int(x) for x in input().split()] # 세로, 가로
# ice_map = []
# for _ in range(N):
#     ice_map.append([int(x) for x in input()])

N, M = 4, 5
ice_map = [[0, 0, 1, 1, 0], [0, 0, 0, 1, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]]


def grassfire(ice_map, i, j):
    global N, M
    if ice_map[i][j] == 1:
        return
    ice_map[i][j] = 1
    if i-1 >= 0:
        grassfire(ice_map, i-1, j)
    if i+1 < N:
        grassfire(ice_map, i+1, j)
    if j-1 >= 0:
        grassfire(ice_map, i, j-1)
    if j+1 < M:
        grassfire(ice_map, i, j+1)

count = 0
for i in range(N):
    for j in range(M):
        if ice_map[i][j] != 1:
            count += 1
            grassfire(ice_map, i, j)

print(count)
