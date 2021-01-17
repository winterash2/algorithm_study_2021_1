from itertools import combinations
import pprint


def rotate_90(array_2d):
    list_of_tuples = zip(*array_2d[::-1])
    return [list(elem) for elem in list_of_tuples]


N, M = [int(x) for x in input().split()]
city = []
for _ in range(N):
    city.append([int(x) for x in input().split()])

chickens = []
houses = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            houses.append([i, j])
        elif city[i][j] == 2:
            chickens.append([i, j])

distances = []
for chicken in chickens:
    # print("chicken=",chicken)
    distance = []
    for house in houses:
        # print("house=",house)
        distance.append(abs(house[0] - chicken[0]) + abs(house[1]-chicken[1]))
    distances.append(distance)

distance_combinations = list(combinations(distances, M))
min_vals = []
for distances in distance_combinations:
    distances = rotate_90(list(distances))
    min_val = 0
    for distance in distances:
        min_val += min(distance)
    min_vals.append(min_val)

print(min(min_vals))
