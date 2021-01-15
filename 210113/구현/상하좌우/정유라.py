n = int(input())
data = input().split()
x, y = 1, 1

# for i in data:
#     if i == 'R':
#         if row == n:
#             continue
#         else:
#             row += 1
#     elif i == 'L':
#         if row == 1:
#             continue
#         else:
#             row -= 1
#     elif i == 'U':
#         if col == 1:
#             continue
#         else:
#             col -= 1
#     elif i == 'D':
#         if col == n:
#             continue
#         else:
#             col += 1
move_types = ['L','R','U','D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
for direction in data:
    for i in range(len(move_types)):
        if direction == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue
    x, y = nx, ny

print(x, y)