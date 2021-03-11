# http://boj.kr/12865
from collections import deque

n, m = map(int, input().split())
info = []
for _ in range(n):
    w, v = map(int, input().split())
    info.append((w, v))
info.sort()
q = deque(info)
max_value = -int(1e9)

dp = 
print(max_value)