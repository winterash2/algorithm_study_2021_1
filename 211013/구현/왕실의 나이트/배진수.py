now = input()

possible_move = [(2,1), (2,-1), (-2,1), (-2,-1), (1,2), (-1,2), (1,-2), (-1,-2)]
a = 'a'
now_x = int(now[1])-1
now_y = ord(now[0]) - ord(a)

print(type(now_x),now_x, type(now_y), now_y)

result = 0
for move in possible_move:
    dx = now_x + move[0]
    dy = now_y + move[1]
    if 0 <= dx < 8 and 0<= dy < 8:
        result += 1

print(result)