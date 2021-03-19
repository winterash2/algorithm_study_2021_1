N, M = map(int, input().split())
dducks = list(map(int, input().split()))

left = 0
right = max(dducks)
answer = 0
while left <= right:
    mid = (left + right) // 2
    calc = 0
    for dduck in dducks:
        remain = dduck - mid
        if remain > 0:
            calc += remain
    if calc >= M:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)

"""
4 6
19 15 10 17
"""