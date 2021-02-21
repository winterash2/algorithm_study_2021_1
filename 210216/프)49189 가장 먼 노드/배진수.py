from collections import deque


def bfs(start, graph, visited):
    q = deque([[start, 0]])
    while q:
        value = q.popleft()
        v, count = value
        if visited[v] == -1:
            visited[v] = count
            count += 1
            for g in graph[v]:
                q.append([g, count])
            

def solution(n, edge):
    answer = 0
    visited = [-1] * (n+1)
    graph = [[] for _ in range(n+1)]
    
    for e in edge:
        a, b = e
        graph[a].append(b)
        graph[b].append(a)

    bfs(1, graph, visited)
    for visit in visited:
        if visit == max(visited):
            answer += 1        
    return answer

"""
테스트 1 〉	통과 (0.03ms, 10.4MB)
테스트 2 〉	통과 (0.04ms, 10.3MB)
테스트 3 〉	통과 (0.10ms, 10.3MB)
테스트 4 〉	통과 (0.87ms, 10.2MB)
테스트 5 〉	통과 (5.72ms, 10.5MB)
테스트 6 〉	통과 (20.71ms, 11.5MB)
테스트 7 〉	통과 (2125.77ms, 20MB)
테스트 8 〉	통과 (5646.76ms, 20.2MB)
테스트 9 〉	통과 (6338.26ms, 24.9MB)
"""