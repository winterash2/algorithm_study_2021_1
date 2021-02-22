# http://boj.kr/1016
import math


# 시간초과.. 
min_num, max_num = map(int, input().split())
arr = [1] * (max_num-min_num+1)
sqrt_num = 2
# count = 0
while True:
    # 제곱한 값이 최대값보다 크면 종료
    if sqrt_num*sqrt_num > max_num:
        break

    # 범위 안의 숫자들을 돌면서 제곱수로 나눠지는지 확인
    for num in range(min_num, max_num+1):
        if num % (sqrt_num*sqrt_num) == 0:
            arr[num-min_num] = 0

    sqrt_num += 1

# print("arr:", arr)
# for i in arr:
#     if i==1:
#         count += 1
print(sum(arr)) # 이런 방법이..








# 이거 틀렸음
# 메모리초과 
# 소수 제곱근 끼리의 최소공배수 ex)4, 9 => 36 두번 빠짐 

# def is_prime_number(n):
#     new_n = int(math.sqrt(n))
#     array = [True for i in range(new_n+1)]

#     # 에라토스테네스의 체
#     print("new n:",  new_n)
#     for i in range(2, int(math.sqrt(new_n))+1):
#         if array[i] == True:
#             j = 2
#             while i*j <= new_n:
#                 array[i*j] = False
#                 j += 1
#     # 범위 안의 소수들 리스트
#     prime_arr = [i for i in range(2, new_n+1) if array[i]]
#     prime_sqr_arr = []

#     # 범위 안에 드는 소수들의 제곱 리스트 
#     for j in prime_arr:
#         if j*j  < n:
#             prime_sqr_arr.append(j*j)
#     return prime_sqr_arr

# arr = is_prime_number(max_num)

# cnt = 0
# for i in arr:
#     cnt += max_num // i # 제곱으로 나눠지는 개수
# print(max_num - cnt)