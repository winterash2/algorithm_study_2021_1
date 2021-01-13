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
import timeit

# 정확성: 42.9 테스트케이스 전부 통과 뜨기는 함
# 효율성: 7.1
# 합계: 50.0 / 100.0
def solution(food_times, k):
    food_times_org = food_times
    answer = 0

    minus = 0
    while True:
        food_len = len(food_times)
        if food_len == 0:
            answer = -1
            return answer
        food_min = min(food_times)
        
        if k >= food_min * food_len:
            food_times = [
                food_time-food_min for food_time in food_times if food_time != food_min]
            minus += food_min
            k -= food_min * food_len
        else:
            break

    k = k % len(food_times)

    count = 0
    for i, food_time in enumerate(food_times_org):
        if food_time > minus:
            if count == k:
                answer = i+1
                return answer
            count += 1

# 테스트 코드
# start = timeit.default_timer()
# end = timeit.default_timer()
# print("min len 측정     %f초 걸렸습니다." % (end - start))

# food_times=[4,2,3,6,7,1,5,8]
# k=16
# answer = 3
food_times = [4, 2, 3, 6, 7, 1, 5, 8]
k = 27
# answer = 5
print(solution(food_times, k))
