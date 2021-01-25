# 당연히 에러를 예상하고 조합으로 풀었으나 역시 메모리 초과로 실패...
#  from itertools import combinations

# n, c = map(int, input().split())
# house = []
# for _ in range(n):
#     house.append(int(input()))

# house.sort()
# combi = list(combinations(house, c))
# result = -1e9
# for arr in combi:
#     min_sum = 1e9
#     for i in range(1,len(arr)):
#         min_sum = min(min_sum ,arr[i] - arr[i-1])
#     result = max(result, min_sum)

# print(result)


## 시작 지점에 들어가는 값으로 문제 해설에서는 house[1] - house[0]로 나와있지만 
# 간격의 최소값은 모르기 때문에 집은 서로다른 위치에 있다고 했으므로 start = 1이 되어야 함
n, c = map(int, input().split())
house = []
for _ in range(n):
    house.append(int(input()))

house.sort()
start = 1
end = house[-1] - house[0]
result = 0

while start <= end:
    mid = (start + end) // 2
    temp = house[0]
    count = 1
    for i in range(1,n):
        if house[i] >= mid + temp:
            count += 1
            temp = house[i]
    
    if count >= c:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
