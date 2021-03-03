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

G = int(input())
P = int(input())

parent = [i for i in range(G+1)]
planes = []
for i in range(P):
    planes.append(int(input()))

cnt = 0
for plane in planes:
    root = find(parent, plane)
    if root == 0:
        break
    else:
        union(parent, root, root - 1)
        cnt += 1

print(cnt)
