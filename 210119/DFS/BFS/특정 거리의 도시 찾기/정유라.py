from collections import deque

n, m, k, x = map(int, input().split())  

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)

distance = [-1] *(n+1)
distance[x] = 0

queue = deque([x])
while queue:
    now = queue.popleft()
    
    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now]+1
            queue.append(next_node)

check = False
for node in range(1, n+1):
    if distance[node] == k:
        print(node)
        check = True
if check == False:
    print(-1)
