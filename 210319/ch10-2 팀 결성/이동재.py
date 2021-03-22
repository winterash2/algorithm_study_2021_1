N, M = map(int, input().split())
insts = []
for _ in range(M):
    inst, a, b = map(int, input().split())
    insts.append((inst, a, b))

# print(insts)

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

parent = [i for i in range(N+1)]
for inst, a, b in insts:
    if inst == 0: # 팀 합치기
        union(parent, a, b)
    else: # 같은 팀 여부 확인
        if find(parent, a) == find(parent, b):
            print("YES")
        else:
            print("NO")

"""
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
"""