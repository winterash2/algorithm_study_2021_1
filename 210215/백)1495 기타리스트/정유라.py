# http://boj.kr/1495


n, s, m = map(int, input().split())

v = list(map(int, input().split()))
volume = [[0] * (m+1) for _ in range(n+1)]
p = s
volume[0][s] = 1
# n: 곡 번호, m: 볼륨

# i(행): i번째 노래, j(열): i번쨰가 가질수 있는 볼륨
for i in range(1, n+1):
    for j in range(m+1):
        if volume[i-1][j] == 0:
            continue
        if j - v[i-1] >= 0:
            volume[i][j-v[i-1]] = 1
        if  j + v[i-1] <= m:
            volume[i][j+v[i-1]] = 1
# for i in range(n):
#     print(volume[i], end="\n")
result = -1
# 맨 마지막 줄 끝에서부터 확인하면서 최댓값출력
for i in range(m, -1, -1):
    if volume[n][i] == 1:
        result = i
        break
print(result)