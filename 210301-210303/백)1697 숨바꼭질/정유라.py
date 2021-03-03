# http://boj.kr/1697
from collections import deque

n, k = map(int, input().split())
visited = [0] * 100001
q = deque([(n, 0)]) # k, sec = 0

while q:
    now, sec = q.popleft()
    if now == k:
        print(sec)
        break
    visited[now] = 1

    if now -1 >= 0 and visited[now-1] == 0:
        q.append((now-1, sec+1))
    if now + 1 < len(visited) and visited[now+1] == 0:
        q.append((now+1, sec+1))
    if now * 2 < len(visited) and visited[now*2] == 0:
        q.append((now*2, sec+1))
    
