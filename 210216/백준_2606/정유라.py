# http://boj.kr/2606
from collections import deque

n = int(input())
m = int(input())

graph = [[0]*(n+1) for _ in range(n+1)]

q = deque()

# 간선 정보 입력 받기
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

    # 컴퓨터가 1일 때 큐에 저장
    if a == 1: 
        q.append(b)
    if b == 1:
        q.append(a)

# 감염된 컴퓨터 배열
computer = [0] * (n+1)
computer[1] = 1 # 어차피 마지막에 1컴퓨터가 감염시킨 컴퓨터들만 세기 때문에 안해도 되긴 함

while q:
    pc = q.popleft()

    computer[pc] = 1
    # 새롭게 감염된 컴퓨터에 연결된 컴퓨터들 찾기
    for i in range(1, n+1): 
        if computer[i] == 1:
            continue
        if graph[pc][i] == 1:
            q.append(i)

print(computer.count(1) -1)
