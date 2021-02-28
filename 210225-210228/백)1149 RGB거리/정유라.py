# http://boj.kr/1149

houses = []
n = int(input())
for _ in range(n):
    houses.append(list(map(int, input().split())))

for i in range(1, n):
    houses[i][0] += min(houses[i-1][1], houses[i-1][2])
    houses[i][1] += min(houses[i-1][0], houses[i-1][2])
    houses[i][2] += min(houses[i-1][0], houses[i-1][1])

print(min(houses[n-1][0], houses[n-1][1], houses[n-1][2]))