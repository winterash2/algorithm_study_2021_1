# 최소 신장 트리 만들기
# 크루스칼 알고리즘 288page


# 1. 간선 데이터를 비용에 따라 오름차순으로 정렬한다.
# 2. 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인한다.
#   2-1. 사이클이 발생하지 않는 경우 최소 신장트리에 포함
#   2-2. 발생하면 포함x
# 3. 모든 간선에 대하여 2번 과정 반복

"""
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4
"""

# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
    print("come in")
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    
# 집의 개수(노드의 개수)와 길의 개수(간선)의 개수 입력받기
n, m = map(int, input().split())
parent = [0] * (n+1)

# 자기 자신으로 부모노드 초기화
for i in range(n+1):
    parent[i] = i

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

# 모든 간선 정보 입력 받기
for i in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort() # 비용이 적은 순으로 정렬
last = 0 # 두 마을로 분리하기 위해서 비용이 제일 큰 마지막 값만 총 비용에서 빼주면 됨
print("edges:", edges)
for edge in edges:
    cost, a, b = edge
    print("cost:", cost, "a:", a, "b:", b)
    # 사이클이 발생하지 않는 경우에만 트리에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        print("?cost?:", cost)
        union_parent(parent, a, b)
        result += cost
        last = cost

print(result - last)