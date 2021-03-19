from itertools import permutations
from collections import deque

def ctrl(board, x0, y0, dx, dy):
    for i in range(1, 4):
        if 0 <= (x1 := x0 + dx * i) < 4 and 0 <= (y1 := y0 + dy * i) < 4:
            if board[x1][y1] > 0:
                return (x1, y1)
            l = i
    return (x0 + dx * l, y0 + dy * l)

def move(board, xy0, xy1):
    dist = [[6] * 4 for _ in range(4)]
    q = deque([(xy0, 0)])
    while q:
        [x, y], d = q.popleft()
        if d < dist[x][y]:
            dist[x][y] = d
            for dx, dy in [(+1, 0), (-1, 0), (0, +1), (0, -1)]:
                if 0 <= x + dx < 4 and 0 <= y + dy < 4:
                    q.append(((x + dx, y + dy), d + 1))
                    q.append((ctrl(board, x, y, dx, dy), d + 1))
    return dist[xy1[0]][xy1[1]]

def solution(board, r, c):
    loc = {k: [] for k in range(1, 7)}
    for i in range(4):
        for j in range(4):
            if board[i][j]:
                loc[board[i][j]].append((i, j))
    minv = 100
    for p in permutations(filter(lambda v: v, loc.values())):
        sumv = 0
        xys = [(r, c)]
        stage = [[v for v in w] for w in board]
        for xy1, xy2 in p:
            vs = [(move(stage, xy, xy1) + move(stage, xy1, xy2), xy2) for xy in xys]\
               + [(move(stage, xy, xy2) + move(stage, xy2, xy1), xy1) for xy in xys]
            stage[xy1[0]][xy1[1]] = stage[xy2[0]][xy2[1]] = 0
            sumv += 2 + (mvn := min(vs)[0])
            xys = [xy for m, xy in vs if m == mvn]
        minv = min(sumv, minv)
    return minv


# 내 풀이
# 고수의 답을 보고 공부를 하는 편이 좋을 것 같다...
"""
from collections import deque
from itertools import permutations
import copy

all_paths = []


def goto(board, start, end):
    q = deque()
    q.append(start)
    visited = [[False for _ in range(4)] for _ in range(4)]
    result = 0
    while q:
        for _ in range(len(q)):
            cur = q.popleft()
            if cur[0] == end[0] and cur[1] == end[1]:
                # print(board)
                # print("goto", start, "to", end, "=", result)
                return result
            x, y = cur[0], cur[1]
            if visited[y][x]:
                continue
            visited[y][x] = True
            # 위
            if y > 0:
                # 위로 한 칸
                q.append((x, y-1))
                # 위로 쭉
                ny = y
                while True:
                    ny = ny - 1
                    if ny == 0 or board[ny][x] != 0:
                        break
                q.append((x, ny))
            # 아래
            if y < 3:
                # 아래로 한 칸
                q.append((x, y+1))
                # 아래로 쭉
                ny = y
                while True:
                    ny = ny + 1
                    if ny == 3 or board[ny][x] != 0:
                        break
                q.append((x, ny))
            # 왼쪽
            if x > 0:
                # 왼쪽으로 한 칸
                q.append((x-1, y))
                # 왼쪽으로 쭉
                nx = x
                while True:
                    nx = nx - 1
                    if nx == 0 or board[y][nx] != 0:
                        break
                q.append((nx, y))
            # 오른쪽
            if x < 3:
                # 오른쪽으로 한 칸
                q.append((x+1, y))
                # 오른쪽으로 쭉
                nx = x
                while True:
                    nx = nx + 1
                    if nx == 3 or board[y][nx] != 0:
                        break
                q.append((nx, y))
        result += 1


def create(p, locs, result):
    global all_paths
    temp = []
    if not p:
        all_paths.append(result)
    else:
        cur = p[0]
        p = p[1:]
        temp = copy.copy(result)
        temp.append(locs[cur][0])
        temp.append(locs[cur][1])
        create(p, locs, temp)
        temp = copy.copy(result)
        temp.append(locs[cur][1])
        temp.append(locs[cur][0])
        create(p, locs, temp)


def create_all_paths(per, locs, result):
    for p in per:
        create(p, locs, [])


def solution(board, r, c):
    board_orig = copy.deepcopy(board)
    answer = 0
    cards = set()
    locs = [[] for _ in range(7)]
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                cards.add(board[i][j])
                locs[board[i][j]].append((j, i))
    cards = list(cards)
    per = list(permutations(cards, len(cards)))
    per = [list(x) for x in per]

    create_all_paths(per, locs, all_paths)
    # [print(x) for x in all_paths]

    answer = 1e9
    # print(goto((0, 3), (2, 3)))
    for paths in all_paths:
        board = copy.deepcopy(board_orig)
        calc = 0
        cur = (c, r)
        for path in paths:
            calc += goto(board, cur, path)
            board[path[1]][path[0]] = 0
            cur = path
        # print(calc)
        answer = min(answer, calc)
    answer += len(all_paths[0])

    return answer
"""


board = [[1, 0, 0, 3],
         [2, 0, 0, 0],
         [0, 0, 0, 2],
         [3, 0, 1, 0]]
r = 1
c = 0
print(solution(board, r, c))

# 내꺼                                     고수꺼
# 테스트 1 〉	통과 (6.52ms, 10.4MB)       테스트 1 〉	    통과 (6.35ms, 10.3MB)
# 테스트 2 〉	통과 (4.84ms, 10.4MB)       테스트 2 〉	    통과 (6.87ms, 10.3MB)
# 테스트 3 〉	통과 (5.04ms, 10.5MB)       테스트 3 〉	    통과 (5.87ms, 10.4MB)
# 테스트 4 〉	통과 (3.74ms, 10.4MB)       테스트 4 〉	    통과 (6.73ms, 10.4MB)
# 테스트 5 〉	통과 (37.67ms, 10.4MB)      테스트 5 〉	    통과 (30.93ms, 10.4MB)
# 테스트 6 〉	통과 (40.69ms, 10.4MB)      테스트 6 〉	    통과 (27.35ms, 10.4MB)
# 테스트 7 〉	통과 (46.81ms, 10.4MB)      테스트 7 〉	    통과 (31.60ms, 10.3MB)
# 테스트 8 〉	통과 (43.37ms, 10.5MB)      테스트 8 〉	    통과 (35.17ms, 10.3MB)
# 테스트 9 〉	통과 (539.67ms, 11MB)       테스트 9 〉	    통과 (200.07ms, 10.3MB)
# 테스트 10 〉	통과 (596.12ms, 11MB)       테스트 10 〉	통과 (198.43ms, 10.3MB)
# 테스트 11 〉	통과 (438.41ms, 11MB)       테스트 11 〉	통과 (174.59ms, 10.3MB)
# 테스트 12 〉	통과 (473.57ms, 11MB)       테스트 12 〉	통과 (291.76ms, 10.4MB)
# 테스트 13 〉	통과 (7696.20ms, 20MB)      테스트 13 〉	통과 (1402.41ms, 10.4MB)
# 테스트 14 〉	통과 (8365.22ms, 19.9MB)    테스트 14 〉	통과 (1967.15ms, 10.3MB)
# 테스트 15 〉	통과 (6293.10ms, 20.1MB)    테스트 15 〉	통과 (1465.48ms, 10.3MB)
# 테스트 16 〉	통과 (7455.70ms, 19.9MB)    테스트 16 〉	통과 (1502.02ms, 10.2MB)
# 테스트 17 〉	통과 (0.22ms, 10.4MB)       테스트 17 〉	통과 (0.51ms, 10.4MB)
# 테스트 18 〉	통과 (0.21ms, 10.5MB)       테스트 18 〉	통과 (0.52ms, 10.3MB)
# 테스트 19 〉	통과 (0.80ms, 10.4MB)       테스트 19 〉	통과 (1.57ms, 10.3MB)
# 테스트 20 〉	통과 (0.63ms, 10.4MB)       테스트 20 〉	통과 (1.60ms, 10.3MB)
# 테스트 21 〉	통과 (37.28ms, 10.5MB)      테스트 21 〉	통과 (56.99ms, 10.3MB)
# 테스트 22 〉	통과 (8893.28ms, 20MB)      테스트 22 〉	통과 (1272.13ms, 10.3MB)
# 테스트 23 〉	통과 (7981.22ms, 20MB)      테스트 23 〉	통과 (1461.34ms, 10.3MB)
# 테스트 24 〉	통과 (49.97ms, 10.4MB)      테스트 24 〉	통과 (31.11ms, 10.3MB)
# 테스트 25 〉	통과 (8771.45ms, 19.9MB)    테스트 25 〉	통과 (2088.72ms, 10.3MB)
# 테스트 26 〉	통과 (48.05ms, 10.5MB)      테스트 26 〉	통과 (34.03ms, 10.3MB)
# 테스트 27 〉	통과 (49.37ms, 10.6MB)      테스트 27 〉	통과 (27.38ms, 10.3MB)
# 테스트 28 〉	통과 (5.28ms, 10.4MB)       테스트 28 〉	통과 (7.62ms, 10.4MB)
# 테스트 29 〉	통과 (4.66ms, 10.4MB)       테스트 29 〉	통과 (6.33ms, 10.4MB)
# 테스트 30 〉	통과 (4.58ms, 10.3MB)       테스트 30 〉	통과 (6.31ms, 10.4MB)