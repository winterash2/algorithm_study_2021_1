N, M = map(int, input().split())
roads = []
total_len = 0
for _ in range(M):
    X, Y, Z = map(int, input().split())
    roads.append((X, Y, Z))

roads.sort(key=lambda x : x[2])

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

parent = [i for i in range(N)]
saved_len = 0
for X, Y, Z in roads:
    if find(parent, X) != find(parent, Y):
        union(parent, X, Y)
    else:
        saved_len += Z

print(saved_len)

"""
7 11
0 1 7
0 3 5
1 2 8
1 3 9
1 4 7
2 4 5
3 4 15
3 5 6
4 5 8
4 6 9
5 6 11
"""