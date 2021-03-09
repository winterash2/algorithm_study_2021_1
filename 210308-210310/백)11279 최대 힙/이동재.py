import heapq
import sys
input = sys.stdin.readline

N = int(input())
q = []
result = []

for _ in range(N):
    x = int(input())
    if x == 0:
        if q:
            result.append(heapq.heappop(q))
        else:
            result.append(0)
    else:
        heapq.heappush(q, -x)

[print(-x) for x in result]