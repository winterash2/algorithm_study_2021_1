def solution(clothes):
    answer = 1
    hashmap = {}
    for cloth in clothes:
        v, k = cloth
        if k not in hashmap:
            hashmap[k] = [v]
        elif k in hashmap:
            hashmap[k].append(v)
    
    keys = hashmap.keys()
    for key in keys:
        answer *= len(hashmap[key]) + 1

    return answer - 1


"""
from itertools import combinations
from functools import reduce

def solution(clothes):
    answer = 0
    hashmap = {}
    for cloth in clothes:
        answer += 1
        v, k = cloth
        if k not in hashmap:
            hashmap[k] = [v]
        elif k in hashmap:
            hashmap[k].append(v)
    data = []
    for v in hashmap.values():
        data.append(len(v))
    # print(data)
    # data = [4, 5, 6, 7]
    length = len(data)
    if length > 1:
        for i in range(2, length + 1):
            arrs = list(combinations(data, i))
            for a in arrs:
                answer += reduce(lambda x, y: x * y, a)
    return answer

"""
clothes = [['yellow_hat', 'headgear'], [
    'blue_sunglasses', 'headgear'], ['green_turban', 'headgear']]
print(solution(clothes))
