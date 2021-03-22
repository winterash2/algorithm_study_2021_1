N, M = map(int, input().split())
x, y, head = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

# [print(x) for x in arr]
directions = [(0, -1), (1, 0), (0, 1), (-1, 0),
              (0, -1), (1, 0), (0, 1), (-1, 0)]
answer = 1
while True:
    isMove = False
    for h in range(head + 3, head - 1, -1):
        nx = x + directions[h][0]
        ny = y + directions[h][1]
        if arr[ny][nx] == 0:
            arr[ny][nx] = 2  # 2는 이미 가본 곳
            x = nx
            y = ny
            head = h % 4
            isMove = True
            answer += 1
            break
    if not isMove:
        nx = x - directions[h][0]
        ny = y - directions[h][1]
        if arr[ny][nx] == 1:
            break
        else:
            x = nx
            y = ny
print(answer)
"""
5 5
1 1 0
1 1 1 1 1
1 0 1 0 1
1 0 0 0 1
1 1 0 0 1
1 1 1 1 1
"""
"""
5 6
1 1 0
1 1 1 1 1 1
1 0 1 0 0 1
1 0 0 1 0 1
1 1 0 0 0 1
1 1 1 1 1 1
"""
"""
5 7
1 1 0
1 1 1 1 1 1 1
1 0 1 0 0 0 1
1 0 0 1 0 1 1
1 1 0 0 0 1 1
1 1 1 1 1 1 1
"""
