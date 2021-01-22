# https://www.acmicpc.net/problem/18310

n = int(input())

houses = list(map(int, input().split()))
# total = 0
# distance = []

# for i in range(n):
#     for j in range(n):
#         if i == j:
#             continue
#         total += abs(houses[i] - houses[j])
#     distance.append(total)

# 바보가튼 나..
houses.sort()
print(houses[(n-1)//2])


