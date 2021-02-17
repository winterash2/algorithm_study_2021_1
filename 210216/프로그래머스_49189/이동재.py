# 테스트 1 〉	통과 (0.02ms, 10.3MB)
# 테스트 2 〉	통과 (0.03ms, 10.3MB)
# 테스트 3 〉	통과 (0.05ms, 10.3MB)
# 테스트 4 〉	통과 (0.46ms, 10.2MB)
# 테스트 5 〉	통과 (1.35ms, 10.5MB)
# 테스트 6 〉	통과 (3.12ms, 10.9MB)
# 테스트 7 〉	통과 (26.53ms, 17.1MB)
# 테스트 8 〉	통과 (42.85ms, 20.2MB)
# 테스트 9 〉	통과 (34.81ms, 20.4MB)
from collections import deque

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    distances = [1e9 for _ in range(n+1)]
    distances[0] = 0

    q = deque()
    q.append(1)
    dist = 0
    while q:
        for _ in range(len(q)):
            currNode = q.popleft()
            if distances[currNode] < 1e9:
                continue
            distances[currNode] = dist
            for nextNode in graph[currNode]:
                q.append(nextNode)
        dist += 1

    answer = distances.count(max(distances))
    return answer

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
