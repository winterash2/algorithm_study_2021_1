def rotate(arr, query):
    y1, x1, y2, x2 = query
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1
    start = arr[y1][x1]
    result = start
    x, y = x1, y1
    while True:
        if y >= y2:
            break
        result = min(result, arr[y+1][x])
        arr[y][x] = arr[y+1][x]
        y += 1
    while True:
        if x >= x2:
            break
        result = min(result, arr[y][x+1])
        arr[y][x] = arr[y][x+1]
        x += 1
    while True:
        if y <= y1:
            break
        result = min(result, arr[y-1][x])
        arr[y][x] = arr[y-1][x]
        y -= 1
    while True:
        if x <= x1:
            break
        result = min(result, arr[y][x-1])
        arr[y][x] = arr[y][x-1]
        x -= 1
    arr[y][x+1] = start

    return result


def solution(rows, columns, queries):
    answer = []
    arr = [[0 for _ in range(columns)] for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            arr[i][j] = i * columns + j + 1

    for query in queries:
        result = rotate(arr, query)
        answer.append(result)

    return answer


# rows = 6
# columns = 6
# queries = [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]

rows = 3
columns = 3
queries = [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]

rows = 3
columns = 5
queries = [[1, 1, 2, 2]]

print(solution(rows, columns, queries))