N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for i in range(1, N+1):
    graph[i] = [0] + list(map(int, input().split()))
plans = list(map(int, input().split()))

parent = [i for i in range(N+1)]


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


for i in range(1, N+1):
    for j in range(i+1, N+1):
        if graph[i][j] == 1:
            union(parent, i, j)

root = find(parent, plans[0])
enable = True
for plan in plans[1:]:
    if find(parent, plan) != root:
        enable = False
        break

if enable:
    print("YES")
else:
    print("NO")

"""
5 4
0 1 0 1 1
1 0 1 1 0
0 1 0 0 0
1 1 0 0 0
1 0 0 0 0
2 3 4 3
"""
