from itertools import combinations
n, m = 5, 3
city = [
    [0, 0, 1, 0, 0],
    [0, 0, 2, 0, 1],
    [0, 1, 2, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 2]
]

house = []
chicken = []

for r in range(n):
    city = list(map(int, input().split()))
    for c in range(n):
        if city[c] == 1:
            house.append((r,c))
        elif city[c] == 2:
            chicken.append((r,c))

candidates = list(combinations(chicken, m))
print("c", candidates)

def get_sum(candidate):
    result = 0

    for hx, hy in house:
        temp = 1e9
        for cx, cy in chicken:
            temp = min(temp, abs(hx-cx)+abs(hy-cy))
        result += temp
    return result

result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))

print(result)