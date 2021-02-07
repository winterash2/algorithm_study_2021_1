# 273page 기본적인 서로소 집합 알고리즘 소스코드




# 부모 노드 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합을 찾기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 팀(노드의 개수)와 팀원(간선의 개수) 입력받기
n, m = map(int, input().split())
parent = [0] * (n+1)
# 자기 자신을 부모로 초기화
for i in range(1, n+1):
    parent[i] = i


# 0, 1 값에 따라 union연산 or 팀 찾기
for i in range(m):
    num, a, b = map(int, input().split())
    if num == 0:
        union_parent(parent, a, b)
    elif num == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")
