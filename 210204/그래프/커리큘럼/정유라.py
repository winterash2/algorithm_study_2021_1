# 위상정렬 알고리즘 296page


# 1. 진입차수가 0인 노드를 큐에 넣는다.
# 2. 큐가 빌 때까지 다음의 과정 반복
#   2-1. 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거
#   2-2. 새롭게 진입차수가 0이 된 노드를 큐에 삽입

"""
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1
"""

from collections import deque
import copy

# 노드의 개수와 간선의 개수 입력 받기
n = int(input())

# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (n+1)
lec_time = [0] * (n+1)
# 각 노드에 연결된 간선 정보를 담기위한 연결리스트(그래프) 초기화
graph = [[] for i in range(n+1)]


# 방향 그래프의 모든 간선 정보를 입력받기
for i in range(1, n+1):
    input_data = list(map(int, input().split()))
    lec_time[i] = input_data[0]

    for j in input_data[1:-1]:
        graph[j].append(i)
        indegree[i] += 1
print(">>", indegree)
print("graph", graph)
# for _ in range(e):
#     a, b = map(int, input().split())
#     graph[a].append(b) # A->B

#     # 진입차수 +1
#     indegree[b] += 1

# 위상 정렬 함수
def topology_sort():
    result = copy.deepcopy(lec_time) # 알고리즘 수행결과를 담을 리스트
    q = deque() # 진입차수가 0인 노드들이 들어올 큐

    # 시작 - 진입차수가 0인 노드 큐에 삽입
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
    
    # 큐가 빌 때까지 반복
    while q:
        now = q.popleft()
        
        # 해당 노드의 간선 제거
        for i in graph[now]:
            result[i] = max(result[i], result[now]+lec_time[i])
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)
    
    # 위상 정렬을 수행한 결과 출력
    for i in range(1, n+1):
        print(result[i])    
topology_sort()