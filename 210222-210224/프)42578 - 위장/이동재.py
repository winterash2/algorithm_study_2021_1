# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.01ms, 10MB)
# 테스트 3 〉	통과 (0.01ms, 10.2MB)
# 테스트 4 〉	통과 (0.01ms, 10.2MB)
# 테스트 5 〉	통과 (0.01ms, 10.2MB)
# 테스트 6 〉	통과 (0.01ms, 10.2MB)
# 테스트 7 〉	통과 (0.01ms, 10.2MB)
# 테스트 8 〉	통과 (0.01ms, 10.1MB)
# 테스트 9 〉	통과 (0.01ms, 10.3MB)
# 테스트 10 〉	통과 (0.01ms, 10.3MB)
# 테스트 11 〉	통과 (0.01ms, 10.1MB)
# 테스트 12 〉	통과 (0.01ms, 10.2MB)
# 테스트 13 〉	통과 (0.01ms, 10.3MB)
# 테스트 14 〉	통과 (0.01ms, 10.2MB)
# 테스트 15 〉	통과 (0.01ms, 10.3MB)
# 테스트 16 〉	통과 (0.00ms, 10.3MB)
# 테스트 17 〉	통과 (0.01ms, 10.2MB)
# 테스트 18 〉	통과 (0.01ms, 10.1MB)
# 테스트 19 〉	통과 (0.01ms, 10.2MB)
# 테스트 20 〉	통과 (0.01ms, 10.2MB)
# 테스트 21 〉	통과 (0.01ms, 10.2MB)
# 테스트 22 〉	통과 (0.01ms, 10.2MB)
# 테스트 23 〉	통과 (0.01ms, 10.2MB)
# 테스트 24 〉	통과 (0.01ms, 10.2MB)
# 테스트 25 〉	통과 (0.01ms, 10.2MB)
# 테스트 26 〉	통과 (0.01ms, 10.2MB)
# 테스트 27 〉	통과 (0.01ms, 10.2MB)
# 테스트 28 〉	통과 (0.01ms, 10.2MB)
def solution(clothes):
    answer = 1
    kindOfClothes = dict()
    for cloth in clothes:
        _ , kind = cloth
        if kind in kindOfClothes: # 여기서 try except 문 쓰면 시간 더 오래 걸림
            kindOfClothes[kind] += 1
        else:
            kindOfClothes[kind] = 1

    values = kindOfClothes.values()

    for v in values: # 있거나 없거나 조합
        answer *= (v+1) # 1 더하는 이유는 안 입는 경우도 포함하기 위해
    answer -= 1 # 마지막에 하나 빼는 이유는 하나라도 입어야 하니까
    
    return answer



# 조합 이용...
# 바보같이 어렵게 생각함
"""
# 테스트 1 〉	실패 (시간 초과)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (0.08ms, 10.3MB)
# 테스트 4 〉	통과 (115.42ms, 10.2MB)
# 테스트 5 〉	통과 (0.07ms, 10.4MB)
# 테스트 6 〉	통과 (0.02ms, 10.3MB)
# 테스트 7 〉	통과 (115.68ms, 10.2MB)
# 테스트 8 〉	통과 (1.25ms, 10.2MB)
# 테스트 9 〉	통과 (0.02ms, 10.1MB)
# 테스트 10 〉	통과 (0.01ms, 10.3MB)
# 테스트 11 〉	통과 (0.03ms, 10.2MB)
# 테스트 12 〉	통과 (3.66ms, 10.3MB)
# 테스트 13 〉	통과 (14.08ms, 10.2MB)
# 테스트 14 〉	통과 (0.03ms, 10.3MB)
# 테스트 15 〉	통과 (0.01ms, 10.2MB)
# 테스트 16 〉	통과 (0.01ms, 10.2MB)
# 테스트 17 〉	통과 (0.02ms, 10MB)
# 테스트 18 〉	통과 (0.14ms, 10.3MB)
# 테스트 19 〉	통과 (1.15ms, 10.2MB)
# 테스트 20 〉	통과 (0.01ms, 10.1MB)
# 테스트 21 〉	통과 (0.01ms, 10.2MB)
# 테스트 22 〉	통과 (0.01ms, 10.2MB)
# 테스트 23 〉	통과 (0.02ms, 10.3MB)
# 테스트 24 〉	통과 (0.02ms, 10.1MB)
# 테스트 25 〉	통과 (0.61ms, 10.2MB)
# 테스트 26 〉	통과 (233.63ms, 10.3MB)
# 테스트 27 〉	통과 (0.01ms, 10.2MB)
# 테스트 28 〉	통과 (0.56ms, 10.3MB)

from itertools import combinations

def solution(clothes):
    answer = 1
    kindOfClothes = dict()
    for cloth in clothes:
        _ , kind = cloth
        if kind in kindOfClothes:
            kindOfClothes[kind] += 1
        else:
            kindOfClothes[kind] = 1

    values = kindOfClothes.values()
    for v in values:
        answer += v
    for i in range(2, len(values) + 1):
        comb = combinations(values, i)
        for c in comb:
            mul = 1
            for elem in list(c):
                mul *= elem
            answer += mul
    return answer

print(solution([["yellow_hat", "headgear"], [
      "blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))
"""