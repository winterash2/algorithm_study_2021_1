n = int(input())
k = int(input())
data = [[0] * (n+1) for _ in range(n+1)]
info = []
for i in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1

l = int(input())
for _ in range(l):
    a, c = input().split()
    info.append((int(a),c))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
    if c == "L":
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

x, y = 1, 1
data[x][y] = 2
result = 0
index = 0
direction = 0
q = [(x, y)]

while True:
    print(x,y)
    nx = x + dx[direction]
    ny = y + dy[direction]

    if 1 <= nx <= n and 1 <= ny <= n and data[nx][ny] != 2:
        if data[nx][ny] == 1:
            data[nx][ny] = 2
            q.append((nx,ny))
        elif data[nx][ny] == 0:
            data[nx][ny] = 2
            q.append((nx,ny))
            px, py = q.pop(0)
            data[px][py] = 0
        
    else:
        result += 1
        break

    x, y = nx, ny
    result += 1
    if info[index][0] == result and index < 1:
        direction = turn(direction, info[index][1])
        index += 1
print(result)
print(info)
print(q)