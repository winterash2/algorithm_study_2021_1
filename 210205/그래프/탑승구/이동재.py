G = int(input())
P = int(input())
datas = []
for _ in range(P):
    datas.append(int(input()))

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

parent = [i for i in range(G+1)]
count = 0
for data in datas:
    root = find(parent, data)
    if root == 0:
        break
    else:
        union(parent, root-1, root)
        count += 1

print(count)

"""
4
6
2
2
3
3
4
4
"""