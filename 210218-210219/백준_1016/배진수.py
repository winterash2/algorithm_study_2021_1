"""
import math
start, end = map(int, input().split())

cnt = 0
for i in range(start, end+1):
    if math.sqrt(i) != int(math.sqrt(i)):
        cnt += 1
    else:
        continue
print(cnt)
"""
from math import sqrt
start, end = map(int, input().split())
cnt = end - start + 1
for i in range(int(sqrt(start)), int(sqrt(end)) + 1):
    if start <= (i * i) <= end:
        cnt -= 1
    else:
        continue

print(cnt)
### 아무리봐도 맞는데 왜 틀렸다고 할까ㅠㅠ
