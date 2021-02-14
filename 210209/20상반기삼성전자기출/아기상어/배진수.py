from collections import deque
import sys
input = sys.stdin.readline


def find(x, y, shark, q, time, eat):
    if arr[x][y] < shark and arr[x][y] == 0:
        q.append((time, x, y, eat))
        return

    for i in range(4):
        dx = x + mx[i]
        dy = y + my[i]
        if 0 <= dx < n and 0 <= dy < n:
            if arr[dx][dy] > shark:
                continue
            elif arr[dx][dy] == shark or arr[dx][dy] == 0:
                time += 1
                find(dx, dy, shark, q, time, eat)
                time -= 1
            else:
                if eat < shark:
                    eat += 1
                    time += 1
                    shark += 1
                    arr[dx][dy] = 0
                    find(dx, dy, shark, q, time, eat)
                elif eat == shark:
                    eat = 0
                    shark += 1
                    time += 1
                    arr[dx][dy] = 0
                    find(dx, dy, shark, q, time, eat)


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
    q = []
    deq = find(x, y, shark, q, time, eat)
    if deq == None:
        break
    else:
        deq.sort()
        deq = deque(deq)
        time, tx, ty, eat = deq.popleft()
        time += t
        x, y = tx, ty

print(time)
