T = int(input())
for _ in range(T):
    H, W = map(int, input().split())
    graph = []
    visited = [[False for _ in range(W)] for _ in range(H)]
    for _ in range(H):
        graph.append(list(input()))
    keys = [x.upper() for x in list(input()) if x != '0']
    keys = set(keys)

    q = []
    for y in range(H):
        for x in range(W):
            if y == 0 or x == 0 or y == H-1 or x == W-1:
                if graph[y][x] == '.' or graph[y][x] == '$':
                    q.append((x, y))
                elif graph[y][x] == '*':
                    pass
                else:
                    if graph[y][x].isupper():
                        q.append((x, y))
                    else:
                        keys.add(graph[y][x])
                        q.append((x,y))
                        graph[y][x] = '.'

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    answer = 0
    blocked = []
    count = 0
    while q:
        changed = False
        while q:
            x, y = q.pop()
            visited[y][x] = True
            if graph[y][x] == '.':
                pass  # 그냥 지나감
            elif graph[y][x] == '$':
                graph[y][x] = '.'
                answer += 1
            elif graph[y][x].islower():  # 키일때
                keys.add(graph[y][x].upper())
                graph[y][x] = '.'
                changed = True
            else:  # 문일때
                if graph[y][x] not in keys:
                    blocked.append((x, y))
                    continue
                else:
                    graph[y][x] = '.'
            for d in directions:
                nx, ny = x + d[0], y + d[1]
                if 0 <= nx < W and 0 <= ny < H:
                    if graph[ny][nx] != '*':
                        if not visited[ny][nx]:
                            q.append((nx, ny))
        if not changed:
            break
        q = q + blocked
        blocked = []

    # [print(''.join(x)) for x in graph]
    print(answer)

# 1차 시도중 문제가 있을거 같아서 방법을 바꿔보려고 함
# 여기서 시도한 방법은 입구로부터 어딘가에 도달할 때 필요한 키들을 저장해놓고
# 나중에 한 번에 처리하려고 함
# 하지만 이렇게 할 경우 같은 곳에 다른 방법으로 도달하려고 할 때 문제가 생길 것 같아서
# 다른 방법을 생각해보기로 하고 넘어감
"""
T = int(input())
for _ in range(T):
    H, W = map(int, input().split())
    graph = []
    for _ in range(H):
        graph.append(list(input()))
    keys = [x.upper() for x in list(input()) if x != '0']
    keys = set(keys)

    q = []
    for y in range(H):
        for x in range(W):
            if y == 0 or x == 0 or y == H-1 or x == W-1:
                if graph[y][x] == '.':
                    q.append((x, y, []))

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    needKeyForKey = []
    needKeyForDoc = []
    while q:
        x, y, need = q.pop()
        if graph[y][x] == '*':  # 벽이면 스킵
            continue
        if graph[y][x] == '.':  # 길이면 이동
            pass
        elif graph[y][x] == '$':  # 문서면 이동과 획득
            needKeyForDoc.append((x, y, need))
        else: # 문이거나 키면 이동과 기록
            if graph[y][x].isupper():  # 문
                need.append(graph[y][x])
            else:  # 키
                needKeyForKey.append((graph[y][x], need))

        for d in directions:
            nx = x + d[0]
            ny = y + d[1]
            if 0 <= nx < W and 0 <= ny < H:
                q.append(nx, ny, need)
    print("needKeyForKey", needKeyForKey)
    print("needKeyForDoc", needKeyForDoc)
"""
