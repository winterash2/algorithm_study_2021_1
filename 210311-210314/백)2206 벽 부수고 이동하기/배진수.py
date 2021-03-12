from collections import deque
import sys
input = sys.stdin.readline
answer = 0

mx = [0, 0, -1, 1]
my = [1, -1, 0, 0]

n, m = map(int, input().split())
arr = []
for _ in range(n):
    x = input().rstrip()
    arr.append(list(x))

visit = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(2)]
visit[0][0][0] = 1

q = deque()
q.append((0, 0, 1, 1))
while q:
    x, y, distance, wall = q.popleft()
    if x == n-1 and y == m-1:
        answer = distance
        break
    else:
        for i in range(4):
            dx = x + mx[i]
            dy = y + my[i]
            if 0 <= dx < n and 0 <= dy < m:
                if visit[wall][dx][dy] == 0:
                    if arr[dx][dy] == '0':
                        visit[wall][dx][dy] = 1
                        q.append((dx, dy, distance+1, wall))
                    elif arr[dx][dy] == '1' and wall:
                        visit[wall][dx][dy] = 1
                        q.append((dx, dy, distance+1, 0))

if answer == 0:
    print(-1)
else:
    print(answer)
