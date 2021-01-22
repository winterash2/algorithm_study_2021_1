from collections import deque
import sys
input = sys.stdin.readline
print = sys.stdout.write

n, m, k, x = map(int, input().split())  
graph = [[] for _ in range(n+1)]

# 도로 정보 입력받기
for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)

# 특정 도시에서 각 도시까지 최단 거리 구하기 위한 배열
distance = [-1] *(n+1)
distance[x] = 0 # 자기 위치 초기화

# bfs 이용
queue = deque([x])
print("Q", queue)
while queue:
    now = queue.popleft()
    
    for next_node in graph[now]:
        # 방문하지 않은 도시
        if distance[next_node] == -1:
            distance[next_node] = distance[now]+1
            queue.append(next_node) # 큐에 삽입

check = False
# 최단 거리가 k인 도시들 출력
for node in range(1, n+1):
    if distance[node] == k:
        print(node)
        check = True
# 없으면 -1 출력
if check == False:
    print(-1)
