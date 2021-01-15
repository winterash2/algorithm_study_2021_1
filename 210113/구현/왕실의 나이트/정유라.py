n = input()
col = int(n[1]) # 1
row = ord(n[0])-96 # a -> 1
# print(x,y)

# HLU : Horizontal Left Up
# VRD : Vertical Right Down
move_types = ['HLU','HLD','HRU','HRD','VLU','VLD','VRU','VRD']
dc = [-1, 1, -1, 1, -2, 2, -2, 2]
dr = [-2, -2, 2, 2, -1, -1, 1, 1]

count = 0

for i in range(8):
    nc = col + dc[i]
    nr = row + dr[i]
    if nc < 1 or nc > 8 or nr < 1 or nr > 8:
        pass
    else:
        count += 1

print(count)