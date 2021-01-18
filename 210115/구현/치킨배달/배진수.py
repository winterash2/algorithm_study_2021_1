from itertools import combinations # 조합을 사용하기 위해 import

n, m = map(int, input().split())

house = []
chicken = []
for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1:
            house.append((i,j)) # 집 위치 정보 입력
        elif data[j] == 2:
            chicken.append((i,j)) # 치킨집 위치 정보 입력

chains = list(combinations(chicken, m)) # 치킨집 중 m개를 뽑는 조합의 수 받음

def find_road(chain): # 조합에 담긴 체인점에서의 집까지의 거리를 더한 정보를 반환하는 함수
    c_road = 0
    for hx, hy in house:
        temp = n+n # 거리는 거리의 최대값(n+n)을 넘지 않음
        for cx, cy in chain:
            temp = min(temp, abs(hx-cx) + abs(hy-cy))
        c_road += temp
    return c_road

result = (n+n) * len(house) # 최대의 값은 거리의 최대값(n+n) * 집의 갯수를 넘지 않음
for chain in chains:
    result = min(result, find_road(chain))

print(result)