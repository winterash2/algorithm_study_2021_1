import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i],i+1))
    
    times = 0
    count_times = 0
    food_num = len(food_times)
    while times + (q[0][0] - count_times)*food_num <= k:
        now = heapq.heappop(q)[0]
        times += (now - count_times)*food_num
        count_times = now
        food_num -= 1

    result = sorted(q, key=lambda x: x[1])
    return result[(k-times)%food_num][1]

food_times = [3,1,2]
k = 5

print(solution(food_times, k))