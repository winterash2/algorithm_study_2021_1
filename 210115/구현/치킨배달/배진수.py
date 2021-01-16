from itertools import combinations


n, m = map(int, input().split())

house = []
chicken = []
for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1:
            house.append((i,j))
        elif data[j] == 2:
            chicken.append((i,j))

chains = list(combinations(chicken, m))

def find_road(chain):
    c_road = 0
    for hx, hy in house:
        temp = 1e9
        for cx, cy in chain:
            temp = min(temp, abs(hx-cx) + abs(hy-cy))
        c_road += temp
    return c_road

result = 1e9
for chain in chains:
    result = min(result, find_road(chain))

print(result)