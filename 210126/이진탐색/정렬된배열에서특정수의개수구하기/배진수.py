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
