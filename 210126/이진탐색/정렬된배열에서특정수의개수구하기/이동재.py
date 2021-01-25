# 가장 먼저 나온거로부터 좌우로 순차로 찾는 방법
# 극단적인 경우에 시간 초과가 뜰 것 같음
"""
N, x = map(int, input().split())
data = list(map(int, input().split()))

# 가장 먼저 찾은 x의 인덱스를 index 변수에, 못 찾으면 -1
start = 0
end = len(data) - 1
index = -1
while start <= end:
    mid = (start + end) // 2
    if data[mid] == x:
        index = mid
        break
    elif data[mid] > x:
        end = mid - 1
    else:
        start = mid + 1

# x를 못 찾으면 -1 출력
if index == -1:
    print("-1")
else:
    count = 1
    # index 보다 작은 것들 순차탐색
    temp = index - 1
    while True:
        if temp < 0 or data[temp] != x:
            break
        count += 1
        temp -= 1
    # index 보다 큰 것들 순차탐색
    temp = index + 1
    while True:
        if temp >= N or data[temp] != x:
            break
        count += 1
        temp += 1
    print(count)
"""