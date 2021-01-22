# 매 차례마다 정렬해주니깐 런타임 에러 ㅠㅠ
# heapq 우선순위 큐 씁시다

# n = int(input())
# cards = []
# for _ in range(n):
#     cards.append(int(input()))

# total = 0
# def cal(cards):
#     global total
#     # print(cards, total)
#     if len(cards) == 1:
#         return cards
#     cards.sort()
#     cards.append(cards[0] + cards[1])
#     total += (cards[0] + cards[1])
#     cards.remove(cards[0])
#     cards.remove(cards[0])
#     cal(cards)

# cal(cards)
# print(total)

import heapq

n = int(input())
cards = []
for _ in range(n):
    heapq.heappush(cards, int(input()))

result = 0

while len(cards) != 1:
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    result += (a+b)
    heapq.heappush(cards, (a+b))

print(result)
