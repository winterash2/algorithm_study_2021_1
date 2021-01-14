def solution(food_times, k):
    # 음식 번호
    index = len(food_times)

    # k초 
    count = 0
    while True:
        i = count % index
        if count == k+1:
            answer = i+1
            break
        food_times[i] -= 1
        count += 1
        
    return answer
print(solution([3,1,2], 5))