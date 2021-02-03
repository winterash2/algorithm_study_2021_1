# N 125짜리 랜덤배열 1000개를 돌릴 때 총 걸린 시간
# dj 110.677533초 걸렸습니다.
# db 90.118793초 걸렸습니다.
# 평균내면 dj 0.110677533
# 평균내면 db 0.090118793

import heapq
from pprint import pprint
import sys
import timeit
import random
input = sys.stdin.readline


dj = 0
db = 0
count = 0
# start = timeit.default_timer()
# T = int(input())
T = 1000
for _ in range(T):
    # N = int(input())
    # graph = [[] for _ in range(N)]
    # for i in range(N):
    #     graph[i] = list(map(int, input().split()))

    N = 125
    n = 125
    graph = [[random.randrange(1,10) for _ in range(N)] for _ in range(N)]

    # dj 시작 -----------------------------------------------------------------
    start = timeit.default_timer()

    INF = float('inf')
    dp = [[INF for _ in range(N)] for _ in range(N)]
    q = []
    heapq.heappush(q, (0, 0, 0))
    while q:
        energy, x, y = heapq.heappop(q)
        if energy >= dp[x][y]:
            continue
        dp[x][y] = energy
        if x-1 >= 0:
            heapq.heappush(q, (graph[x][y] + energy, x-1, y))
        if x+1 < N:
            heapq.heappush(q, (graph[x][y] + energy, x+1, y))
        if y-1 >= 0:
            heapq.heappush(q, (graph[x][y] + energy, x, y-1))
        if y+1 < N:
            heapq.heappush(q, (graph[x][y] + energy, x, y+1))
    answer_dj = dp[N-1][N-1] + graph[N-1][N-1]
    # print(answer)

    end = timeit.default_timer()
    dj += (end - start)

    # db 시작 -----------------------------------------------------------------
    start = timeit.default_timer()

    INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # 최단 거리 테이블을 모두 무한으로 초기화
    distance = [[INF] * n for _ in range(n)]

    x, y = 0, 0 # 시작 위치는 (0, 0)
    # 시작 노드로 가기 위한 비용은 (0, 0) 위치의 값으로 설정하여, 큐에 삽입
    q = [(graph[x][y], x, y)]
    distance[x][y] = graph[x][y]

    # 다익스트라 알고리즘을 수행
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보를 꺼내기
        dist, x, y = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[x][y] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 맵의 범위를 벗어나는 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            cost = dist + graph[nx][ny]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))
    answer_db = distance[n - 1][n - 1]
    # print(answer)

    end = timeit.default_timer()
    db += (end - start)

    if answer_dj != answer_db:
        print("정답 아님")
        break
    count += 1
    print(count)

print("dj %f초 걸렸습니다." % dj)
print("db %f초 걸렸습니다." % db)
