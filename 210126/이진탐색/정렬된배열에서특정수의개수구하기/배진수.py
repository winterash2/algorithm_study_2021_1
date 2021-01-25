n, x = map(int, input().split())
sorting = list(map(int, input().split()))

def search(sorting, val, start, end):
    while start < end:
        mid = (start + end) // 2
        print(mid)
        if sorting[mid] == val:
            return mid
        elif val < sorting[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return False

result = search(sorting, x, 0, len(sorting))
if result == False:
    print(-1)

else:
    left = 0
    left = result
    right = 0
    right = result
    while sorting[left] == x:
        left -= 1
    while sorting[right] == x:
        right += 1
    print(right - left - 1)

#####################################################################
# 파이썬 만세

from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
array = list(map(int, input().split()))

def count_by(array, left, right):
    right = bisect_right(array, right)
    left = bisect_left(array, left)
    return right - left

count = count_by(array, x, x)

if count == 0:
    print(-1)
else:
    print(count)