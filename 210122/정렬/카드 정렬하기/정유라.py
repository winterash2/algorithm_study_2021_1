import heapq

n = int(input())
heap = []
for _ in range(n):
    data = int(input()) 
    heapq.heappush(heap, data)


result = 0

#힙에 원소가 한 개 남을 때까지
while len(heap) != 1:
    #가장 작은 두 개의 카드 묶음 꺼내기
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)

    # 더하고 다시 넣기
    sum_val = one + two
    result += sum_val
    heapq.heappush(heap, sum_val)

print(result)
