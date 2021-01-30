n = int(input())
triangle = []

for _ in range(n):
    triangle.append(list(map(int, input().split())))

for i in range(n-2, -1, -1):
    for j in range(i+1):
        temp = max(triangle[i+1][j], triangle[i+1][j+1])
        triangle[i][j] += temp

print(triangle[0][0])
