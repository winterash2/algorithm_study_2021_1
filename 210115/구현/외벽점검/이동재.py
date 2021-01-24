from itertools import permutations
from pprint import pprint as pprint

# 1차 시도 - 책 안 보고
# 2배로 늘린다는 아이디어를 파이썬에서는 리스트를 -n~n-1 로 반복할 수 있다는 점을 사용하려고 했는데
# 그냥 개 어려워지긴 함... 실패...
def solution(n, weak, dist):
    answer = 0
    weak_len = len(weak)
    dist_len = len(dist)

    weak_detail = []
    for i in range(len(weak)):
        right = weak[i+1] - \
            weak[i] if i != len(weak) - 1 else n - weak[i] + weak[0]
        weak_detail.append((weak[i], right))
    # pprint(weak_detail)
    dist_permu = list(permutations(dist))
    # pprint(dist_permu)

    min_friend = 1e9
    for i in range(len(weak_detail) * -1, 1, 1):
        # print(i, weak_detail[i])
        for dists in dist_permu:
            # print("-"*50)
            count_friend = 0
            dist_temp = list(dists)
            weak_curr = i
            dist_curr = 0
            while True:
                # print("weak_curr=", weak_curr, "dist_curr=", dist_curr)
                if weak_detail[weak_curr][1] > dist_temp[dist_curr]:
                    weak_curr += 1
                    dist_curr += 1
                else:
                    dist_temp[dist_curr] -= weak_detail[weak_curr][1]
                    weak_curr += 1
                if weak_curr >= i + 4:
                    dist_curr = dist_curr if dist_curr != 0 else 1
                    if dist_curr < min_friend:
                        min_friend = dist_curr
                    break
                if dist_curr >= 4:
                    break
    answer = min_friend
    return answer


n, weak, dist, result = 12, [1, 5, 6, 10], [1, 2, 3, 4], 2
print(solution(n, weak, dist))


# 좌우 전부 한거
"""
    for i in range(len(weak)):
        left = weak[i] - weak[i-1] if i != 0 else weak[i] - weak[i-1] + n
        right = weak[i+1] - \
            weak[i] if i != len(weak) - 1 else n - weak[i] + weak[0]
        weak_detail.append((left, i, right))
    pprint(weak_detail)
"""
