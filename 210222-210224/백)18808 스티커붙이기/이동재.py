def rotate_90(array_2d):
    list_of_tuples = zip(*array_2d[::-1])
    return [list(elem) for elem in list_of_tuples]


def get_possible_pos(graph, sticker):
    for baseX in range(len(graph)-len(sticker)+1):
        for baseY in range(len(graph[0])-len(sticker[0])+1):
            enable = True
            for i in range(len(sticker)):
                for j in range(len(sticker[0])):
                    if sticker[i][j] == 1:
                        if graph[baseX+i][baseY+j] == 1:
                            enable = False
                            break
                if not enable:
                    break
            if enable:
                return (baseX, baseY)
    return None


def attach_sticker(graph, sticker, pos):
    x, y = pos
    for i in range(len(sticker)):
        for j in range(len(sticker[0])):
            if sticker[i][j] == 1:
                graph[x+i][y+j] = 1


N, M, K = map(int, input().split())
graph = [[0 for _ in range(M)] for _ in range(N)]
stickers = []
for _ in range(K):
    sticker = []
    R, C = map(int, input().split())
    for i in range(R):
        sticker.append(list(map(int, input().split())))
    stickers.append(sticker)

for sticker in stickers:
    for _ in range(4):
        # print("-"*20)
        # [print(sticker[i]) for i in range(len(sticker))]
        # print("-"*20)
        pos = get_possible_pos(graph, sticker)
        if pos:
            attach_sticker(graph, sticker, pos)
            break
        sticker = rotate_90(sticker)
    # [print(graph[i]) for i in range(len(graph))]

answer = 0
for g in graph:
    answer += sum(g)
print(answer)

"""
5 4 4
3 3
1 0 1
1 1 1
1 0 1
2 5
1 1 1 1 1
0 0 0 1 0
2 3
1 1 1
1 0 1
3 3
1 0 0
1 1 1
1 0 0
"""
