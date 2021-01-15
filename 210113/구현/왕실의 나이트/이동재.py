col, row = input()
row = int(row)
col = int(ord(col)) - int(ord('a')) + 1

moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
count = 0
for move in moves:
    if 8 >= (row - move[0]) >= 1:
        if 8 >= (col - move[1]) >= 1:
            count += 1

print(count)