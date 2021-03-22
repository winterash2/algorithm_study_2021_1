def solution(dirs):
    dirs = list(dirs)
    answer = set()
    x = y = 0
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    for head in dirs:
        if head == 'U':
            d = 0
        elif head == 'D':
            d = 1
        elif head == 'L':
            d = 2
        elif head == 'R':
            d = 3

        nx = x + directions[d][0]
        ny = y + directions[d][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            answer.add((min(x, nx), max(x, nx), min(y, ny), max(y, ny)))
            x = nx
            y = ny
    print(answer)
    answer = len(answer)

    return answer

dirs = "ULURRDLLU"
print(solution(dirs))