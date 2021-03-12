from collections import deque
import sys
input = sys.stdin.readline
check = True

mx = [0,0,-1,1]
my = [1,-1,0,0]

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

visit = [[0]*m for _ in range(n)]
visit[0][0] = 1

q = deque()
q.append((0,0))
answer = -1
while q:
    x, y = q.popleft()
    for i in range(4):
        dx = x + mx[i]
        dy = y + my[i]
        if 0<= dx < n and 0<= dy < m:
            if visit[dx][dy] == 1:
                continue
            
