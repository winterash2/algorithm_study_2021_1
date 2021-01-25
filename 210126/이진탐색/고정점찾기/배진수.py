n = int(input())
array = list(map(int, input().split()))

def search_stick(array, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == mid:
            return mid
        elif array[mid] < mid:
            start = mid + 1
        else:
            end = mid - 1
    return False

result = search_stick(array, 0, len(array) - 1)
if result == False:
    print(-1)
else:
    print(result)