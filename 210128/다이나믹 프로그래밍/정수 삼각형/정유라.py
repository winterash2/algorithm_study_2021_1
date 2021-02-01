# n = int(input())
n = 5

array = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
# for i in range(n):
#     array.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(len(array[i])):
        # 왼쪽 위에서 내려옴
        if j == 0:
            up_left = 0
        else:
            up_left = array[i-1][j-1]
        
        # 바로 위에서 내려옴
        if j == i:
            up = 0
        else:
            up = array[i-1][j]

        # 최대 합 저장
        array[i][j] = array[i][j] + max(up_left, up)

print(max(array[n-1]))