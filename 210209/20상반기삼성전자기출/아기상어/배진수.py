import sys
input = sys.stdin.readline

mx = [-1, 0, 0, 1]
my = [0, -1, 1, 0]

def check(arr):
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0:
                return False
    return True


def bfs(x, y, q, time, shark, moved, eat):
    global count
    if time > count:
        return
    if arr[x][y] < shark and arr[x][y] != 0:
        # arr[x][y] = 0
        count = min(count, time)
        q.append((time, x, y, eat, shark))
        return

    else:
        for i in range(4):
            dx = x + mx[i]
            dy = y + my[i]
            if 0 <= dx < n and 0 <= dy < n:
                if (dx, dy) in moved:
                    continue

                if arr[dx][dy] > shark:
                    moved.append((dx,dy))
                    continue
                elif arr[dx][dy] == 0 or arr[dx][dy] == shark:
                    time += 1
                    moved.append((dx, dy))
                    bfs(dx, dy, q, time, shark, moved, eat)
                    time -= 1
                    moved.remove((dx, dy))
                else:
                    eat += 1
                    time += 1
                    moved.append((dx, dy))
                    bfs(dx, dy, q, time, shark, moved, eat)
                    time -= 1
                    moved.remove((dx, dy))
                    eat -= 1
    return


n = int(input())

arr = []
mx = [-1, 1, 0, 0]
my = [0, 0, -1, 1]
x, y = 0, 0
for i in range(n):
    input_arr = list(map(int, input().split()))
    for j in range(n):
        if input_arr[j] == 9:
            x, y = i, j
            input_arr[j] = 0
    arr.append(input_arr)

time = 0
shark = 2
eat = 0
while 1:
    print("----------")
    print(time,x,y,shark)
    if check(arr) == True:
        break
    if shark == eat:
        # print("상어진화")
        shark += 1
        eat = 0
    q = []
    moved = []
    count = int(1e9)
    bfs(x, y, q, time, shark, moved, eat)
    if len(q) == 0:
        break
    else:
        print(q)
        q.sort()
        time, tx, ty, eat, shark = q[0]
        arr[tx][ty] = 0
        x, y = tx, ty

print(time)