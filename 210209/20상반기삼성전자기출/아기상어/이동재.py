N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
baits = []
x_shark = 0
y_shark = 0
for i in range(N):
    for j in range(N):
        if 0 < graph[i][j] < 6:
            baits.append((i, j))
        if graph[i][j] == 9:
            x_shark = i
            y_shark = j

def get_distance(a, b):
    return (abs(a[0]-b[0]) + abs(a[1]-b[1]))

# 가장 위, 왼쪽에 있는 물고기를 먹으러 갈 것
# 거리가 적은걸 먼저, y가 작은걸 먼저, x가 작은걸 먼저

def update_all_distance(baits, x, y, size_shark):
    can_baits = []
    for bait in baits:
        if graph[bait[0]][bait[1]] < size_shark:
            can_baits.append((get_distance((bait[0], bait[1]), (x, y)), bait[0], bait[1]))
    return can_baits

time = 0
size_shark = 2
count_eat = 0
while baits:
    if len(baits) == 0:
        break
    can_baits = update_all_distance(baits, x_shark, y_shark, size_shark)
    if len(can_baits) == 0:
        break
    can_baits.sort(key=lambda x : [x[0], x[1], x[2]])
    # baits.sort(key=lambda x : [0, x[1], x[0]])
    # print(can_baits)
    distance, x_shark, y_shark = can_baits[0]
    baits.remove((x_shark, y_shark))
    count_eat += 1
    if count_eat >= size_shark:
        size_shark += 1
        count_eat = 0
    time += distance

print(time)
"""
4
4 3 2 1
0 0 0 0
0 0 9 0
1 2 3 4
"""