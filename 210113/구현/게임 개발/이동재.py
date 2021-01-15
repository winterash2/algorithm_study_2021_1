# n, m = [int(x) for x in input().split()]
# x, y, direction = [int(x) for x in input().split()]

# map_input = []
# for i in range(n):
#     map_input.append([int(x) for x in input().split()])

n = 4
m = 4
x = 1
y = 1
direction = 0
map_input = [
    [1, 1, 1, 1],
    [1, 0, 0, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 1]
]

# 북동남서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

map_check = [[0] * m for _ in range(n)]
map_check[x][y] = 1


def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


count = 1
turn_count = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if map_check[nx][ny] == 0 and map_input[nx][ny] == 0:
        map_check[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_count = 0
        continue
    else:
        turn_count += 1
    if turn_count == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if map_input[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_count = 0

print(count)
