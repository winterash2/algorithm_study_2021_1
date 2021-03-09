# dp를 1부터 M까지 탐색하지 않고 요소가 있는 부분만을 탐색하려고 visited라는 이름의 set을 이용
# 메모리 초과 남
# visited 사용 안 하고 dp를 전부 돌면서 M번 돌아가게 하면 시간초과남
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
mems = list(map(int, input().split()))
costs = list(map(int, input().split()))
INF = float('inf')
dp = [INF for _ in range(M+1)]
visited = set()

for idx in range(N):
    add_visited = set()
    for i in visited:
        if i+mems[idx] >= M:
            dp[M] = min(dp[M], dp[i] + costs[idx])
        else:
            add_visited.add(i+mems[idx])
            dp[i+mems[idx]] = min(dp[i+mems[idx]], dp[i] + costs[idx])
    dp[mems[idx]] = min(dp[mems[idx]], costs[idx])
    add_visited.add(mems[idx])
    visited = visited | add_visited

print(dp[M])

# 재귀로 푼 것
# 시간 초과 뜸
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
mems = list(map(int, input().split()))
costs = list(map(int, input().split()))

answer = 1e9

def solution(idx, mem, cost):
    global answer, mems, costs
    if idx >= N:
        return
    # 현재 idx를 포함
    nmem = mem + mems[idx]
    ncost = cost + costs[idx]
    if nmem >= M:
        answer = min(answer, ncost)
    else:
        solution(idx+1, nmem, ncost)
    # 현재 idx를 포함하지 않음
    solution(idx+1, mem, cost)

solution(0, 0, 0)

print(answer)
"""

# 1차 dp 배열을 안 쓰고 모든 경우를 다 계산할 때
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
mems = list(map(int, input().split()))
costs = list(map(int, input().split()))

dp = []  # [메모리, cost]
for cur in range(N):
    newDp = []
    for mem, cost in dp:
        if mem >= M:
            continue
        newDp.append([mem+mems[cur], cost+costs[cur]])
    dp += dp + newDp
    dp.append([mems[cur], costs[cur]])

answer = 1e9
for mem, cost in dp:
    if mem >= M and cost < answer:
        answer = cost

print(answer)
"""
