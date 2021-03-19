def solution(dirs):
    sizeofnum = 11
    answer = 0
    arr = [[0] * sizeofnum for _ in range(sizeofnum)]
    step = dict(U=[-1, 0],
                L=[0, -1],
                R=[0, 1],
                D=[1, 0])
    x = 5
    y = 5
    dx = 0
    dy = 0
    new_dict = dict()
    for dir in dirs:
        dx = x + step[dir][0]
        dy = y + step[dir][1]
        if 0 <= dx < sizeofnum and 0 <= dy < sizeofnum:
            if str(x) + str(y) not in new_dict and str(dx) + str(dy) not in new_dict:
                new_dict.update({str(x) + str(y): []})
                new_dict[str(x)+str(y)].append(str(dx)+str(dy))
            elif str(x) + str(y) in new_dict:
                if str(dx) + str(dy) not in new_dict[str(x) + str(y)]:
                    new_dict[str(x) + str(y)].append(str(dx) + str(dy))
            elif str(x) + str(y) not in new_dict:
                if str(dx) + str(dy) in new_dict:
                    if str(x)+str(y) not in new_dict[str(dx) + str(dy)]:
                        new_dict[str(dx) + str(dy)].append(str(x)+str(y))
            x = dx
            y = dy
    for key in new_dict.keys():
        answer += len(new_dict[key])
    print(new_dict)
    return answer


# dirs = "LULLLLLLU"
dirs = "UUUDDDDDR"
print(solution(dirs))
