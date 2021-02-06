import sys
input = sys.stdin.readline

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]


n, m = map(int, input().split())
parent = [0] * (n + 1)

for i in range(1, n+1):
    parent[i] = i

for i in range(m):
    check, a, b = map(int, input().split())
    if check == 0:
        union_parent(parent, a, b)
    elif check == 1:
        if find_parent(parent, a) != find_parent(parent, b):
            print("NO")
        else:
            print("YES")
