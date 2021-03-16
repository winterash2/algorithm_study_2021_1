import sys
from collections import deque

n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(input()))

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'R':
            red = [i, j]
            arr[i][j] = '.'
        if arr[i][j] == 'B':
            blue = [i, j]
            arr[i][j] = '.'


def move(mx, my, r_x, r_y, bl_x, bl_y):
    red_copy = [r_x, r_y]
    blue_copy = [bl_x, bl_y]
    r_chk = True
    b_chk = True
    r_cnt = 0
    b_cnt = 0
    while 1:
        if r_chk:
            if arr[red_copy[0] + mx][red_copy[1] + my] == '#':
                r_chk = False
            elif arr[red_copy[0] + mx][red_copy[1] + my] == 'O':
                red_copy[0] = 0
                red_copy[1] = 0
                r_chk = False
            elif arr[red_copy[0] + mx][red_copy[1] + my] == '.':
                red_copy[0] += mx
                red_copy[1] += my
            r_cnt += 1

        if b_chk:
            if arr[blue_copy[0] + mx][blue_copy[1] + my] == '#':
                b_chk = False
            elif arr[blue_copy[0] + mx][blue_copy[1] + my] == 'O':
                blue_copy[0] = 0
                blue_copy[1] = 0
                r_chk = False
            elif arr[blue_copy[0] + mx][blue_copy[1] + my] == '.':
                blue_copy[0] += mx
                blue_copy[1] += my
            b_cnt += 1

        if r_chk == False and b_chk == False:
            if red_copy != [0, 0] and red_copy == blue_copy:
                if b_cnt > r_cnt:
                    return [red_copy[0], red_copy[1], blue_copy[0] - mx, blue_copy[1] - my]
                else:
                    return [red_copy[0] - mx, red_copy[1] - my, blue_copy[0], blue_copy[1]]
            return [red_copy[0], red_copy[1], blue_copy[0], blue_copy[1]]


q = deque()
q.append([1, red[0], red[1], blue[0], blue[1]])
visit = [[[[False] * m for i in range(n)] for i in range(m)] for i in range(n)]
visit[red[0]][red[1]][blue[0]][blue[1]] = True

chk = True
answer = 11
while q:
    cnt, r_x, r_y, bl_x, bl_y = q.popleft()
    if cnt > 10:
        break
    for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        rdx = r_x + d[0]
        rdy = r_y + d[1]
        bdx = bl_x + d[0]
        bdy = bl_y + d[1]
        if arr[rdx][rdy] != '#' or arr[bdx][bdy] != '#':
            rx, ry, bx, by = move(d[0], d[1], r_x, r_y, bl_x, bl_y)
            if bx != 0 and by != 0:
                if rx == 0 and ry == 0:
                    answer = min(answer, cnt)
                    chk = False
                    break
                if not visit[rx][ry][bx][by]:
                    visit[rx][ry][bx][by] = True
                    q.append([cnt+1, rx, ry, bx, by])
if chk == True:
    print(-1)
else:
    print(answer)


"""
10 10
##########
#RB....#.#
#..#.....#
#........#
#.O......#
#...#....#
#........#
#........#
#.......##
##########
"""