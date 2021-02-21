def rotate_90(arr):
    global n, m
    rotate = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            rotate[i][j] = arr[n-j-1][i]
    return rotate


n, m = map(int, input().split())
arr = []
for _ in range(n):
    ss = input()
    data = []
    for s in ss:
        data.append(int(s))
    arr.append(data)

res = rotate_90(arr)
dp = [0] * n

# 못풀겠습니다.. ㅠㅠ