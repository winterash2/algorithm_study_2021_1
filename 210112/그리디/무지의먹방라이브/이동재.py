# 정확성: 37.5
# 효율성: 0.0
# 합계: 37.5 / 100.0
"""
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

# 정확성: 42.9 테스트케이스 전부 통과 뜨기는 함
# 효율성: 7.1
# 합계: 50.0 / 100.0
"""
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
"""


# 깡으로 루프 돌아서하는 방법
# 효율성까지 안 가도 시간초과 뜸
# 정확성: 37.5
# 효율성: 0.0
# 합계: 37.5 / 100.0
"""
def solution(food_times, k):
    food_times_org = food_times
    food_len = len(food_times)
    answer = 0

    i = 0
    while True:
        if food_times[i % food_len] > 0:
            food_times[i % food_len] -= 1
            if k == 0:
                answer = i % food_len + 1
                break
            else:
                k -= 1
        i += 1
    return answer
"""

# 정확성: 42.9
# 효율성: 57.1
# 합계: 100.0 / 100.0
def solution(food_times, k):
    # 시간 내에 다 못 먹는 경우
    if sum(food_times) <= k:
        return -1
    
    # dict 형태로 변경
    food_times_dict = dict()
    for i, time in enumerate(food_times):
        food_times_dict[i+1] = time
    
    # 먹는 시간을 기준으로 정렬 -> 리스트로 만들어서
    def return_value(x):
        return x[1]
    sorted_by_value = sorted(food_times_dict.items(), key=return_value)
    food_len = len(sorted_by_value)
    
    # 빨리 먹을 수 있는것부터 먹어버리기
    # 이전에 먹은게 있으면 그 다음꺼 먹을때 걸리는 시간 계산할때는 이전에 먹은거 다 먹을때까지 걸린 시간만큼 빼야 함
    # 그래서 time=이전꺼 먹는데 걸리는 시간
    time = 0
    for item in sorted_by_value:
        if (food_len * (item[1] - time)) < k:
            k -= (food_len * (item[1] - time))
            food_len -= 1
            time = item[1]
        else:
            break

    # 현재 남아있는 음식 중 몇번째꺼인지 확인
    k = k % food_len

    # 정렬하지 않은 전체 리스트에서 먹는데 걸리는 시간이 time 보다 큰 것들만 골라서 k번째인 것을 찾음
    count = 0
    for i, food_time in enumerate(food_times):
        if food_time > time:
            if count == k:
                answer = i+1
                return answer
            count += 1


# 시간 측정
# import timeit
# start = timeit.default_timer()
# end = timeit.default_timer()
# print("min len 측정     %f초 걸렸습니다." % (end - start))

# 테스트 케이스
# food_times = [3, 1, 2]
# k = 5
food_times=[4,2,3,6,7,1,5,8]
k=16
# answer = 3
# food_times = [4, 2, 3, 6, 7, 1, 5, 8]
# k = 27
# answer = 5
print(solution(food_times, k))
