from itertools import combinations


def check(aisle, N, x, y):
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for d in directions:
        nx = x
        ny = y
        while True:
            nx += d[0]
            ny += d[1]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                break
            elif aisle[nx][ny] == "O":
                break
            elif aisle[nx][ny] == "S":
                return True
    return False


N = int(input())
aisle = []
for _ in range(N):
    aisle.append(list(input().split()))

teachers = []
blanks = []

for x in range(N):
    for y in range(N):
        if aisle[x][y] == "X":
            blanks.append((x, y))
        elif aisle[x][y] == "T":
            teachers.append((x, y))

blanks_combinations = combinations(blanks, 3)

founded = False
for blanks in blanks_combinations:
    for blank in blanks:
        aisle[blank[0]][blank[1]] = "O"
    founded = False
    for teacher in teachers:
        founded = check(aisle, N, teacher[0], teacher[1])
        if founded:
            break
    if not founded:
        break
    for blank in blanks:
        aisle[blank[0]][blank[1]] = "X"
if founded:
    print("NO")
else:
    print("YES")
