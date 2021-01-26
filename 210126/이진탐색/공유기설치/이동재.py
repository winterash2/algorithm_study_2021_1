# 집을 N개나 가지고 있는 도현이... 다주택자... 부럽다...
import sys
input = sys.stdin.readline

N, C = list(map(int, input().split()))
houses = []
for _ in range(N):
    houses.append(int(input()))
houses.sort()


# 해당 거리로 공유기를 설치했을 때 원하는 개수만큼 설치 가능한지 확인하는 함수
def check_possible(houses, length, C):
    prev = -1e11
    for house in houses:
        if house - prev >= length:
            prev = house
            C -= 1
            if C == 0:
                return True
    return False


start = 1  # 갓동빈?... arr[1]-arr[0]는 최소값이 아님...
end = (houses[-1] - houses[0])//(C-1) + 1
result = -1
while start <= end:
    mid = (start+end)//2
    if check_possible(houses, mid, C):
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)
