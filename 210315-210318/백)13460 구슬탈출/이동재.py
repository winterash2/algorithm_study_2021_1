H, W = map(int, input().split())
graph = []
for _ in range(H):
    graph.append(list(input()))

def move_left(graph, red, blue, d):
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)] # 상하좌우
    # red
    rx, ry = red[0], red[1]
    nrx, nry = rx, ry
    bx, by = blue[0], blue[1]
    nbx, nby = bx, by
    while True:
        rx, ry = nrx, nry
        nrx, nry = rx + directions[d][0], ry + directions[d][1]
        if graph[nry][nrx] == '#':
            red = (rx, ry)
        elif graph[nry][nrx] == '.':
            continue
        elif graph[nry][nrx] == 'O':
            return True
        elif graph[nry][nrx] == 'B':
            

def move_right(graph, red, blue):


def move_up(graph, red, blue):


def move_down(graph, red, blue):




"""
5 5
#####
#..B#
#.#.#
#RO.#
#####
"""