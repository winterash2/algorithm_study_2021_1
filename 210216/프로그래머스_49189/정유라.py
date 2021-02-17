from collections import deque

def solution(n, edge):
    # 노드, 간선 정보
    graph = [[] * (n+1) for _ in range(n+1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    # 방문 처리를 위한 배열
    distance = [-1] * (n+1)
    distance[1] = 1 # 시작노드 초기화

    q = deque()
    q.append(1) # 시작 노드 : 1

    while q:
        now = q.popleft()
        for next_node in graph[now]: # now에 딸려있는 노드들에 대해서
            if distance[next_node] == -1: # 방문 안했으면
                q.append(next_node) # 큐에 삽입
                distance[next_node] = distance[now] + 1 # 방문처리 및 거리 갱신
    
    answer = 0
    max_depth = max(distance)
    for i in distance:
        if i == max_depth:
            answer += 1
    

    return answer

edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]	
print(solution(6, edge))