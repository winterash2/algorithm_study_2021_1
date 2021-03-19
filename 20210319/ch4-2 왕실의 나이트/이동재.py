x, y = input()
x = ord(x) - 96
y = int(y)
directions = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
answer = 0
for d in directions:
    nx = x + d[0]
    ny = y + d[1]
    if 1 <= nx <= 8 and 1 <= ny <= 8:
        answer += 1

print(answer)