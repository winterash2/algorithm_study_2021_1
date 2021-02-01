# 내가 heapq로 짠거
# 평균  0.006721519100000008 초
# 갓동빈 코드보다 5배정도 오래 걸림

import heapq

N = int(input())
# N = 1000

ugly_set = set()
hq = []
hq.append(1)

while hq:
    curr = heapq.heappop(hq)
    ugly_set.add(curr)
    if len(ugly_set) >= N:
        break
    if curr*2 not in hq:
        heapq.heappush(hq, curr*2)
    if curr*3 not in hq:
        heapq.heappush(hq, curr*3)
    if curr*5 not in hq:
        heapq.heappush(hq, curr*5)

ugly_list = list(ugly_set)
ugly_list.sort()
print(ugly_list[N-1])


# 갓동빈 코드
# 평균  0.0013529951000000005 초
"""
import timeit

time_avg = 0
for _ in range(1000):
    start = timeit.default_timer()
    # n = int(input())
    n = 1000

    ugly = [0] * n # 못생긴 수를 담기 위한 테이블 (1차원 DP 테이블)
    ugly[0] = 1 # 첫 번째 못생긴 수는 1

    # 2배, 3배, 5배를 위한 인덱스
    i2 = i3 = i5 = 0
    # 처음에 곱셈 값을 초기화
    next2, next3, next5 = 2, 3, 5

    # 1부터 n까지의 못생긴 수들을 찾기
    for l in range(1, n):
        # 가능한 곱셈 결과 중에서 가장 작은 수를 선택
        ugly[l] = min(next2, next3, next5)
        # 인덱스에 따라서 곱셈 결과를 증가
        if ugly[l] == next2:
            i2 += 1
            next2 = ugly[i2] * 2
        if ugly[l] == next3:
            i3 += 1
            next3 = ugly[i3] * 3
        if ugly[l] == next5:
            i5 += 1
            next5 = ugly[i5] * 5

    # n번째 못생긴 수를 출력
    # print(ugly[n - 1])
    end = timeit.default_timer()
    time_avg += end - start

time_avg = time_avg / 1000
print("평균 ", time_avg, "초")
"""
