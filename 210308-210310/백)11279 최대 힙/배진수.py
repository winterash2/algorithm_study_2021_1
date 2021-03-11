import heapq, sys
input = sys.stdin.readline

n = int(input())

q = []
for _ in range(n):
    x = int(input())
    if x == 0:
        if q:
            res = heapq.heappop(q)
            print(-res)
        else:
            print(0)
    else:
        heapq.heappush(q, -x)