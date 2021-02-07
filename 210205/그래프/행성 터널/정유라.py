# 최소 신장 트리 만들기
# 크루스칼 알고리즘 288page


# 1. 간선 데이터를 비용에 따라 오름차순으로 정렬한다.
# 2. 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인한다.
#   2-1. 사이클이 발생하지 않는 경우 최소 신장트리에 포함
#   2-2. 발생하면 포함x
# 3. 모든 간선에 대하여 2번 과정 반복


# 간선의 비용이 min(abs(xA-xB), abs(yA-yB), abs(zA-zB)) 이므로
# 각 좌표에 따라 sort하여 우선순위큐에 넣으면 우선순위큐 안에서 알아서 정렬되고 걔네를 가지고 크루스칼 알고리즘 수행 
import heapq

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

# 초기화
n = int(input())
parent = [0] * n
for i in range(n):
    parent[i] = i 

planet = []
for i in range(n):
    data = list(map(int, input().split()))
    planet.append([i]+data)
# planet: ex) [행성번호, x좌표, y좌표, z좌표]



q = [] 

# x를 기준으로 정렬
planet.sort(key=lambda x:x[1])
for i in range(n-1):
    heapq.heappush(q, [abs(planet[i][1]-planet[i+1][1]), planet[i][0], planet[i+1][0]])     # q에 들어가는 값: (i번째-i+1번째 행성x좌표값차이 절대값, i번째행성번호, i+1번째행성번호)

# y를 기준으로 정렬
planet.sort(key=lambda x:x[2])
for i in range(n-1):
    heapq.heappush(q, [abs(planet[i][2]-planet[i+1][2]), planet[i][0], planet[i+1][0]])

# z를 기준으로 정렬
planet.sort(key=lambda x:x[3])
for i in range(n-1):
    heapq.heappush(q, [abs(planet[i][3]-planet[i+1][3]), planet[i][0], planet[i+1][0]])

result = 0
count = 0
while q:
    cost, a, b = heapq.heappop(q)

    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        count += 1
    if count == n-1:
        break

print(result)
    
