n, k = map(int, input().split())    

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

arr1.sort()             # 오름차순
arr2.sort(reverse=True) # 내림차순

for i in range(k):
    if arr1[i] < arr2[i]:
        arr1[i], arr2[i] = arr2[i], arr1[i]
    else:
        break

print(sum(arr1))

