# 내가 했던 방식
# 방식 자체는 책에서 설명하는 방식과 동일하지만 힙큐를 쓰지 않아서 시간초과됨
import sys
input = sys.stdin.readline
N = int(input())
cards = []
for _ in range(N):
    cards.append(int(input()))
#
def insert_card(cards, number):
    for i in range(len(cards)):
        if cards[i] >= number:
            cards.insert(i, number)


cards.sort()
compare = 0
prev = cards[0]
cards = cards[1:]
while cards:
    c = cards[0]
    cards = cards[1:]
    if prev > c:
        insert_card(cards, prev)
        prev = c
    else:
        prev = prev+c
        compare += prev

print(compare)


# 책 정답 코드
import heapq

N = int(input())
heap = []
for i in range(N):
    data = int(input())
    heapq.heappush(heap, data)

compare = 0
while len(heap) != 1:
    min1 = heapq.heappop(heap)
    min2 = heapq.heappop(heap)
    sum_value = min1 + min2
    compare += sum_value
    heapq.heappush(heap, sum_value)

print(compare)

# 백준 1등 코드
import heapq, sys

N, *heap = map(int, sys.stdin) # 인풋을 최대한 빠르게
result = 0

heapq.heapify(heap) # 간단하게 우선순위 힙으로 만드는 법

while len(heap) > 1:
    n = heapq.heappop(heap) + heapq.heappop(heap)
    result += n
    heapq.heappush(heap, n)

print(result)
