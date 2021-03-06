# 플로이드 워셜

# 초기화 및 간선 정보 입력 받기
n = int(input())    
m = int(input())
INF = int(1e9)
graph = [[INF]*(n+1) for _ in range(n+1)]

# 자기 자신으로 갈 때 0으로 초기화
for a in range(n+1):
    for b in range(n+1):
        if a == b:
            graph[a][b] = 0

for i in range(m):
    a, b, c = map(int, input().split())
    if graph[a][b] > c:  # 최소거리 갱신: INF로 초기화해줬으니 비교해서 c값 넣으면 됨
        graph[a][b] = c
"""
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
3 5 10
3 1 8
1 4 2
5 1 7
3 4 2
5 2 4
"""
# 플로이드 워셜
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if graph[i][j] == INF:
#             print("0", end=" ")
#         else:
#             print(graph[i][j], end=" ")
#     print()

## 배열 출력 편하게하는 방봅
for i in range(1, n+1):
    print(*graph[i][1:])