from collections import deque

n,m,k,x=map(int, input().split())
# n 도시개수           m 도로개수         최단거리가k    x 출발점

road_info=[[] for _ in range(n+1)]

for _ in range(m):
    a, b=map(int, input().split())
    road_info[a].append(b)


distance=[-1]*(n+1)
distance[x]=0

q=deque([x])

while q:
    now=q.popleft()

    for next_node in road_info[now]:
        if distance[next_node]==-1:
            distance[next_node]=distance[now]+1
            q.append(next_node)

check=False
for i in range(1,n+1):
    if distance[i]==k:
        print(i)
        check=True

if check==False:
    print(-1)