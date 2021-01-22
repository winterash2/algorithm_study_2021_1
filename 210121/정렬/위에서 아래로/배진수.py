# 내림차순으로 정렬하는 프로그램

n = int(input())
arr = [0]*n
for i in range(n):
    arr[i] = int(input())

arr.sort(reverse=True)
for i in arr:
    print(i, end=' ')