# 조합 사용해서 풀면 메모리 초과 나옴
# from itertools import combinations

# n = int(input())
# coins = list(map(int, input().split()))
# result = set()

# for i in range(1, n+1):
#     sum_coin = list(combinations(coins, i))
#     for combi in sum_coin:
#         result.add(sum(combi))
# print(result)
# res = len(result) + 1
# for i in range(1,len(result)+1):
#     if i not in result:
#         res = i
#         print(res)
#         break

# if res > len(result):
#     print(res)

n = int(input())
coins = list(map(int, input().split()))

coins.sort()

num = 1
for c in coins:
    if num < c:
        break
    num += c

print(num)