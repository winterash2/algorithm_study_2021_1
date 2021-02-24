import sys
input = sys.stdin.readline


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


n = int(input())
data = [list(input().rstrip()) for _ in range(n)]
parent = [x for x in range(n+1)]
graph = []

total = 0
for i in range(n):
    for j in range(n):
        if data[i][j] == 0:
            graph.append((0, i+1, j+1))
        else:
            if ord('a') <= ord(data[i][j]) <= ord('z'):
                graph.append((ord(data[i][j]) - ord('a') + 1, i+1, j+1))
                total += (ord(data[i][j]) - ord('a') + 1)
            elif ord('A') <= ord(data[i][j]) <= ord('Z'):
                graph.append((ord(data[i][j]) - ord('A') + 27, i+1, j+1))
                total += (ord(data[i][j]) - ord('A') + 27)

graph.sort()
for g in graph:
    lensun, a, b = g
    if lensun == 0:
        continue
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        total -= lensun
    else:
        continue

result = True
for i in range(1, n + 1):
    if find(parent, i) != 1:
        result = False
        
if result:
    print(total)
else:
    print(-1)
