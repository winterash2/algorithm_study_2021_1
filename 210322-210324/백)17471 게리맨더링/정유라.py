# http://boj.kr/17471

# 1. 조합 이용하여 선거구 선정 
# 2. 각 선거구가 이어져있는지 bfs로 확인한다
# 3. 이어져있지 않다면 bfs에서 0을 반환하고 이어져있으면 해당 선거구의 인구를 반환한다
# 4. 인구수 차의 최소값을 계속 기록해나간다
# 5. 마지막에 조건대로 출력

from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline

# def dfs(nnow, now_cnt, area_cnt):
#     global most_min
#     queue = deque([(nnow, now_cnt)])
#     while queue:
#         now, count = queue.popleft()

#         if visited[now] == 0 and now not in area:
#             visited[now] = 1
#             area.append(now)
#             now_cnt += 1
        
#             if now_cnt == area_cnt:
#                 people_in_area = bfs(area)
#                 people_notin_area = bfs([x for x in node if x not in area])

#                 if people_in_area != 0 and people_notin_area != 0:
#                     most_min = min(most_min, abs(people_in_area-people_notin_area))
#                 return
            
#             for next_city in cities[now]:
#                 dfs(next_city, now_cnt, area_cnt)
#                 if len(area) != 0:
#                     area.pop()
#     return
            
def bfs(area):
    global cities
    total = 0
    visited = [0] * (n+1)
    q = deque([area[0]])
    while q:
        now = q.popleft()
        if visited[now] != 0:
            continue
        visited[now] = 1
        total += people[now]
        for next_city in cities[now]:
            if next_city in area:
                if visited[next_city] == 0:
                    q.append(next_city)

    for city in area:
        if visited[city] == 0:
            return 0
    return total


n = int(input())
people = [0] + list(map(int, input().split()))
cities = [[0]]
node = [i for i in range(1, n+1)]

for _ in range(n):
    next_to_cities = list(map(int, input().split()))
    cities.append(next_to_cities[1:])

most_min = int(1e9)

# 리스트 사이 차집합
# a_sub_b = [x for x in a not in b]

for cnt in range(1, n//2+1):
    visited = [0] * (n+1)
    combination = list(combinations(node, cnt))
    
    for area in set(combination):
        people_in_area = bfs(area)
        people_notin_area = bfs([x for x in node if x not in area])

        if people_in_area != 0 and people_notin_area != 0:
            most_min = min(most_min, abs(people_in_area-people_notin_area))

if most_min == int(1e9):
    print(-1)
else:
    print(most_min)



"""
8
17 42 46 81 71 8 37 12
4 2 4 5 7
5 1 3 4 5 8
2 2 4
5 1 2 3 7 8
5 1 2 6 7 8
2 5 8
4 1 4 5 8
5 2 4 5 6 7
"""