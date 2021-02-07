import sys
input = sys.stdin.readline

N, M = map(int, input().split())
roads = []
for _ in range(M):
    A, B, C = map(int, input().split())
    roads.append((C, A, B))

# N, M = 7, 12
# roads = [(3, 1, 2), (2, 1, 3), (1, 3, 2), (2, 2, 5), (4, 3, 4), (6, 7, 3), (5, 5, 1), (2, 1, 6), (1, 6, 4), (3, 6, 5), (3, 4, 5), (4, 6, 7)]

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

roads.sort()
parent = [ i for i in range(N+1) ]
min_cost = 0
max_road = 0
for C, A, B in roads:
    if find(parent, A) == find(parent, B):
        continue
    else:
        union(parent, A, B)
        min_cost += C
        if C > max_road:
            max_road = C

print(min_cost - max_road)