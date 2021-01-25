# 이진 탐색으로 푼 것
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dducks = list(map(int, input().split()))

max_len = max(dducks)

answer = -1
start = 0
end = max_len
while start <= end:
    mid = (start+end)//2
    total_len = 0
    for dduck in dducks:
        total_len += dduck - mid if dduck > mid else 0
    if total_len < M:
        end = mid - 1
    else:
        answer = mid
        start = mid + 1
if answer == -1:
    print("can't")
else:
    print(answer)

# 이진 탐색 없이 풀었던 것
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dducks = list(map(int, input().split()))

dducks.sort(reverse=True)

answer = -1
can_slice = 0
sliced_len = 0
dduck_count = 0
for i in range(max(dducks), -1, -1):
    while dducks[dduck_count] == i:
        dduck_count += 1
        can_slice += 1
    sliced_len += can_slice
    if sliced_len >= M:
        answer = i
        break

if answer == -1:
    print("can't")
else:
    print(answer)
"""
