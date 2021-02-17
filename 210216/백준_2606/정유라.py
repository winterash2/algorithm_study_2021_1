# http://boj.kr/2606
from collections import deque

n = int(input())
m = int(input())

graph = [[0]*(n+1) for _ in range(n+1)]

q = deque()

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
    if a == 1: 
        q.append(b)
    if b == 1:
        q.append(a)

computer = [0] * (n+1)
computer[1] = 1 

while q:
    pc = q.popleft()

    computer[pc] = 1
    for i in range(1, n+1):
        if computer[i] == 1:
            continue
        if graph[pc][i] == 1:
            q.append(i)

print(computer.count(1) -1)
