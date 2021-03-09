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