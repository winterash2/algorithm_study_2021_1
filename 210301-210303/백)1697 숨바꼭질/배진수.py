from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

answer = int(1e9)
move = [1, -1, 2]
q = deque()
visit = [0 for i in range(100001)]
visit[n] = 1
q.append((n, 0))

while q:
    dist, time = q.popleft()
    if dist == k:
        answer = time

    if dist - 1 >= 0 and visit[dist - 1] == 0:
        q.append((dist-1, time + 1))
        visit[dist-1] = 1
    if dist + 1 <= 100000 and visit[dist + 1] == 0:
        q.append((dist+1, time + 1))
        visit[dist+1] = 1
    if dist * 2 <= 100000 and visit[dist * 2] == 0:
        q.append((dist*2, time + 1))
        visit[dist*2] = 1
print(answer)
