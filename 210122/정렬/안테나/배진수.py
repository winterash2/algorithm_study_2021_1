n = int(input())
houses = list(map(int, input().split()))
houses.sort()
print(houses[len(houses)//2-1])
# home = set(houses)

# result = 0
# min_length = 1e9

# for h in home:
#     sum_len = 0
#     for house in houses:
#         sum_len += abs(h-house)
#     print(h, sum_len)
#     if sum_len < min_length:
#         min_length = sum_len
#         result = h
# 동빈이 화나게 하네
