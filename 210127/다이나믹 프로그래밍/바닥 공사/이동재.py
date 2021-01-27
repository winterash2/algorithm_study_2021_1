N = int(input())
tiles = [0] * N

tiles[0] = 1
tiles[1] = 1 + 2
for i in range(2, N):
    tiles[i] = (tiles[i-2]*2 + tiles[i-1]) % 796796
print(tiles[N-1])
