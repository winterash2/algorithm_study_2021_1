# 배열 사용하는 방식으로도 해봤는데 이것도 실패함...
# 어떻게 하는지는 아는데... 구현 문제 진짜... 짜증난다...
import sys
sys.stdout = open('output.txt','w')

C = int(input())

for _ in range(C):
    N = int(input())
    graph = [[0 for _ in range(400)] for _ in range(200)]
    # 방향은 우상향 -> 상향 -> 좌상향 -> 좌하향 -> 하향 -> 우하향 ---- 이걸 2번 반복한 배열을 만들어놓음
    directions = [(1, -1), (0, -2), (-1, -1), (-1, 1), (0, 2), (1, 1), (1, -1), (0, -2), (-1, -1), (-1, 1), (0, 2), (1, 1)]
    idxD = 0
    graph[100][201] = 6
    graph[100][200] = 1
    graph[101][199] = 2
    graph[100][198] = 3
    graph[99][199] = 4
    graph[99][201] = 5
    graph[100][202] = 2
    graph[101][201] = 3
    x = 101
    y = 201
    useCount = [1e9, 0, 0, 0, 0, 0]
    result = [0, 1, 2, 3, 4, 5, 2, 3] + [0 for _ in range(N-7)]
    #7까지 초기화
    for i in range(8, N+1):
        # 방향을 바꿀 수 있는지 확인, 바꿀 수 있으면 다음 방향으로 바꿈
        nx, ny = x + directions[idxD+1][0], y + directions[idxD+1][1]
        if graph[nx][ny] == 0:
            idxD += 1
            if idxD >= 6:
                idxD -= 6
        # 방향을 바꿨거나 안 바꿨거나 어쨋것 이번에 채울 칸 위치
        x, y = x + directions[idxD][0], y + directions[idxD][1]
        cant = [graph[x][y-2], graph[x-1][y-1], graph[x+1][y-1], graph[x-1][y+1], graph[x+1][y+1], graph[x][y+2]]
        canTile = list(set([1,2,3,4,5]) - set([graph[x][y-2], graph[x-1][y-1], graph[x+1][y-1], graph[x-1][y+1], graph[x+1][y+1], graph[x][y+2]]))
        canTile.sort(reverse=True)
        minIdx = 0
        for c in canTile:
            if useCount[c] <= useCount[minIdx]:
                minIdx = c
        graph[x][y] = c
        result[i] = c
    print(result[N])
    [print(graph[i]) for i in range(200)]


# 배열 안 쓰고 해보려고 했는데 실패함
"""
C = int(input())

for _ in range(C):
    N = int(input())

    # 모서리인 요소들
    add = 7
    edges = [2, 3, 4, 5, 6, 7]
    i = 0
    while True:
        nextEdge = edges[i] + add
        edges.append(nextEdge)
        if nextEdge > N:
            break
        i += 1
        add += 1
    # print(edges)

    # 둘레를 감쌀 때 마지막으로 닫는 역할을 하는 요소들
    mul = 2
    circleEnds = [7]
    i = 0
    while True:
        nextCircleEnd = circleEnds[i] + (mul * 6)
        circleEnds.append(nextCircleEnd)
        if nextCircleEnd > N:
            break
        mul += 1
        i += 1
    # print(circleEnds)

    tiles = [0 for _ in range(N+1)]
    tiles[1] = 1
    remainUse = [6 for _ in range(N+1)]  # 모서리가 6개이기 때문에 6번 쓰여야 함
    idxUse = 1
    nextEdgeIdx = 0  # 모서리인지 확인
    nextCircleEndIdx = 0  # 둘레를 감싸는 마지막 요소인지 확인
    useCount = [1e9, 0, 0, 0, 0, 0]
    for i in range(2, N+1):
        # print(i, "-"*20)
        cnt = 2
        if i == edges[nextEdgeIdx]:
            cnt -= 1
            nextEdgeIdx += 1
        if i == circleEnds[nextCircleEndIdx]:
            cnt += 1
            nextCircleEndIdx += 1
        remainUse[i] -= (cnt+1)

        canTile = [1, 2, 3, 4, 5]
        for idx in range(idxUse, idxUse + cnt):
            remainUse[idx] -= 1
            if remainUse[idx] == 0:
                idxUse += 1
            if tiles[idx] in canTile:
                canTile.remove(tiles[idx])

        remainUse[i-1] -= 1
        if tiles[i-1] in canTile:
            canTile.remove(tiles[i-1])
        
        minTileNum = 0
        for c in canTile:
            if useCount[c] < useCount[minTileNum]:
                minTileNum = c

        useCount[minTileNum] += 1
        tiles[i] = minTileNum

    print(tiles[N])
"""
