# N = int(input())
# arr = list(map(int, input().split()))

N, arr = 5, [-15, -6, 1, 3, 7]
N, arr = 7, [-15, -4, 2, 8, 9, 13, 15]
N, arr = 7, [-15, -4, 3, 8, 9, 13, 15]

start = 0
end = len(arr) - 1

result = -1
while start <= end:
    # print(start, end)
    mid = (start + end) // 2
    if arr[mid] == mid:
        result = mid
        break
    elif arr[mid] < mid:
        start = mid + 1
    else:
        end = mid - 1

print(result)
