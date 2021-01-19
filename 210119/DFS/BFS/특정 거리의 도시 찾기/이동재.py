from collections import deque

# 파이썬은 입력에 걸리는 시간이 길어서 입력때문에 시간초과가 뜨기 좋음
# 그런 경우 아래 두 줄을 넣어줘야 함
import sys
input = sys.stdin.readline

N, M, K, X = [int(x) for x in input().split()]
paths = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = [int(x) for x in input().split()]
    paths[A].append(B)

q = deque()
min_path = [1e9 for _ in range(N+1)]

min_path[X] = 0
q.append(X)
while q:
    curr_city = q.popleft()
    if min_path[curr_city] == K:
        continue
    # print(curr_city)
    for next_city in paths[curr_city]:
        #   if min_path[curr_city] + 1 < min_path[next_city]: #   여기 조건을 한 번도 안 갔던 곳이면 으로 바꿔도 됨
        if min_path[next_city] == 1e9:                      # 이렇게 해도 문제 없음. 그 이유는 bfs이기 때문
            q.append(next_city)
            min_path[next_city] = min_path[curr_city] + 1

if min_path.count(K) == 0:
    print("-1")
else:
    for i, m in enumerate(min_path):
        if m == K:
            print(i)
