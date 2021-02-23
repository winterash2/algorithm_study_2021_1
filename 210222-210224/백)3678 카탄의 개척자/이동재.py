
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