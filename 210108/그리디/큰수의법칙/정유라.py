# n = int(input())
# m = int(input())
# k = int(input())

# arr = []
# for i in range(n):
#     arr.append(int(input()))

n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
sum = 0
index = 0
while m > 0:
    for i in range(k):
        if m <= 0:
            break
        sum += arr[n-1]
        m -= 1
    if m <= 0:
        break
    sum += arr[n-2]
    m -= 1

print(sum)