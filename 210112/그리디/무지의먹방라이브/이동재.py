"""
# 정확성: 37.5
# 효율성: 0.0
# 합계: 37.5 / 100.0

def solution(food_times, k):
    answer = 0

    food_num_time_dict = dict()
    for i, time in enumerate(food_times):
        food_num_time_dict[i+1] = time
    
    while True:
        food_min = min(food_num_time_dict.values())
        food_len = len(food_num_time_dict)
        if food_len == 0:
            answer = -1
            return answer
        elif k > food_min * food_len:
            food_num_time_dict = {key: value-food_min for key, value in food_num_time_dict.items() if value != food_min}
            k -= food_min * food_len
        else:
            break
    
    while True:
        food_len = len(food_num_time_dict)
        if k > food_len:
            k -= food_len
        else:
            break
    
    food_num_time_list = sorted(food_num_time_dict)

    if k == len(food_num_time_list):
        answer = food_num_time_list[0]
    else:
        answer = food_num_time_list[k]

    return answer
"""

def solution(food_times, k):
    pass

print(solution([3,1,2], 5))

