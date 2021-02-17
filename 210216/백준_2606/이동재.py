C = int(input())
N = int(input())
links = []
for _ in range(N):
    a, b = map(int, input().split())
    links.append((a, b))

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

parent = [i for i in range(C+1)]
for link in links:
    a, b = link
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)

for i in range(1, C+1):
    find_parent(parent, i)

print(parent.count(1)-1)

"""
7
6
1 2
2 3
1 5
5 2
5 6
4 7
"""