R, C, T = map(int, input().split())
graph = []
for _ in range(R):
    graph.append(list(map(int, input().split())))

# 공청기 위치 확인
for i in range(R):
    if graph[i][0] == -1:
        ACU = (i, 0) # Air coniditioner Up
        ACD = (i+1, 0) # Air conditioner Down
        break


def air_clean_up(graph, ACU):
    row, col = ACU
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    idxD = 0
    row += directions[idxD][0]
    col += directions[idxD][1]
    while True:
        nrow = row + directions[idxD][0]
        ncol = col + directions[idxD][1]
        if nrow > ACU[0] or nrow < 0 or ncol >= C or ncol < 0:
            idxD += 1
            nrow = row + directions[idxD][0]
            ncol = col + directions[idxD][1]
        if (nrow, ncol) == ACU:
            break
        graph[row][col] = graph[nrow][ncol]
        row = nrow
        col = ncol
    graph[row][col] = 0


def air_clean_down(graph, ACD):
    row, col = ACD
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    idxD = 0
    row += directions[idxD][0]
    col += directions[idxD][1]
    while True:
        nrow = row + directions[idxD][0]
        ncol = col + directions[idxD][1]
        if nrow >= R or nrow < ACD[0] or ncol >= C or ncol < 0:
            idxD += 1
            nrow = row + directions[idxD][0]
            ncol = col + directions[idxD][1]
        if (nrow, ncol) == ACD:
            break
        graph[row][col] = graph[nrow][ncol]
        row = nrow
        col = ncol
    graph[row][col] = 0

def dust_spread(graph, R, C):
    new_graph = [[0 for _ in range(C)] for _ in range(R)]
    new_graph[ACU[0]][ACU[1]] = -1
    new_graph[ACD[0]][ACD[1]] = -1
    for r in range(R):
        for c in range(C):
            if graph[r][c] > 0:
                spread = graph[r][c] // 5
                count = 0
                for direction in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                    nr = r + direction[0]
                    nc = c + direction[1]
                    if 0 <= nr < R and 0 <= nc < C and graph[nr][nc] != -1:
                        new_graph[nr][nc] += spread
                        count += 1
                new_graph[r][c] += (graph[r][c] - (spread * count))
    return new_graph


for _ in range(T):
    graph = dust_spread(graph, R, C)
    air_clean_up(graph, ACU)
    air_clean_down(graph, ACD)

# [print(x) for x in graph]
answer = 0
for r in range(R):
    for c in range(C):
        if graph[r][c] > 0:
            answer += graph[r][c]

print(answer)