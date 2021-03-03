import sys
input = sys.stdin.readline

mx = [0, 0, -1, 1]
my = [1, -1, 0, 0]

r, c, t = map(int, input().split())
room = []
monji = []
gongi = []
for i in range(r):
    x = list(map(int, input().split()))
    for j in range(c):
        if x[j] == -1:
            gongi.append(i)
        elif x[j] != 0:
            monji.append((i, j))
    room.append(x)


def cycle(room):
    up, down = gongi
    room[up][0] = 0
    room[down][0] = 0
    # up 수행
    for i in range(up-1, 0, -1):
        room[i][0] = room[i-1][0]
    for j in range(c-1):
        room[0][j] = room[0][j+1]
    for i in range(up):
        room[i][c-1] = room[i+1][c-1]
    for j in range(c-1, 0, -1):
        room[up][j] = room[up][j-1]

    # down 수행
    for i in range(down+1, r-1):
        room[i][0] = room[i+1][0]
    for j in range(c-1):
        room[r-1][j] = room[r-1][j+1]
    for i in range(r-1, down, -1):
        room[i][c-1] = room[i-1][c-1]
    for j in range(c-1, 0, -1):
        room[down][j] = room[down][j-1]


def virus():
    arr = [[0] * c for _ in range(r)]
    for gon in gongi:
        arr[gon][0] = -1

    for x in range(r):
        for y in range(c):
            if room[x][y] > 0:
                cnt = 0
                for k in range(4):
                    dx = x + mx[k]
                    dy = y + my[k]
                    if 0 <= dx < r and 0 <= dy < c and arr[dx][dy] != -1:
                        arr[dx][dy] += (room[x][y] // 5)
                        cnt += 1
                arr[x][y] += (room[x][y] - (room[x][y] // 5) * cnt)
    return arr


for i in range(t):
    room = virus()
    cycle(room)

answer = 0
for i in range(r):
    for j in range(c):
        answer += room[i][j]
print(answer)
