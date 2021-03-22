N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append([int(x) for x in list(input().split()[0])])

# [print(x) for x in arr]
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
answer = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            # print(i, j)
            q = [(i, j)]
            while q:
                x, y = q.pop()
                arr[x][y] = 1
                for d in directions:
                    nx = x + d[0]
                    ny = y + d[1]
                    if 0 <= nx < N and 0 <= ny < M:
                        if arr[nx][ny] == 0:
                            q.append((nx, ny))
            answer += 1
            # print("-----------------------------------------------------")
            # [print(x) for x in arr]

print(answer)
"""
4 5
00110    
00011
11111
00000
"""
"""
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000   
11111111110011
11100011111111
11100011111111
"""