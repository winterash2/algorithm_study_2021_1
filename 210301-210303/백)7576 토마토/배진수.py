from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
box = []
q = deque()
for i in range(n):
    x = list(map(int, input().split()))
    for j in range(m):
        if x[j] == 1:
            q.append((i, j, 0))
    box.append(x)


def check_0(arr):
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                return False
    return True


mx = [0, 0, 1, -1]
my = [1, -1, 0, 0]

while q:
    x, y, cnt = q.popleft()
    for i in range(4):
        nx = x + mx[i]
        ny = y + my[i]
        if 0 <= nx < n and 0 <= ny < m:
            if box[nx][ny] == 0:
                box[nx][ny] = 1
                q.append((nx, ny, cnt+1))
if check_0(box):
    print(cnt)
else:
    print(-1)
