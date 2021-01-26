# bisect 라이브러리를 사용하여 양 끝의 인덱스를 찾아서 구한 코드
import bisect

N, x = map(int, input().split())
data = list(map(int, input().split()))

# N, x = 7,2
# data = [1,1,2,2,2,2,3]
# N, x = 7,4
# data = [1,1,2,2,2,2,3]


def first(arr, val):
    index = bisect.bisect_left(arr, val)
    if index < len(arr) and arr[index] == val:
        return index
    else:
        return None

def last(arr, val):
    index = bisect.bisect_right(arr, val)
    if arr[index - 1] == val:
        return (index - 1)
    else:
        return None

first_index = first(data, x)
if first_index == None:
    print("-1")
else:
    last_index = last(data, x)
    print(last_index - first_index + 1)

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