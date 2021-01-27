import sys
import timeit
# 대충 짠 코드, 책 코드보다 쪼끔 더 오래 걸림
# 시간 0.100997
# """
N, M = map(int, input().split())
values = []
dp = [1e9] * (10000+1)

for _ in range(N):
    val = int(sys.stdin.readline().rstrip())
    values.append(val)
    dp[val] = 1

start = timeit.default_timer()

count = 0
for i in range(M+1):
    for value in values:
        count += 1
        if i-value > 0 and dp[i - value] < 1e9:
            dp[i] = min(dp[i], dp[i - value] + 1)

end = timeit.default_timer()
print("count=", count) # count= 100000
if dp[M] == 1e9:
    print(-1)
else:
    print(dp[M])
print("min len 측정     %f초 걸렸습니다." % (end - start))
# """

"""
# 책 코드
# 걸린 시간 0.073720
# 정수 N, M을 입력 받기
n, m = map(int, input().split())
# N개의 화폐 단위 정보를 입력 받기
array = []
for i in range(n):
    array.append(int(input()))
start = timeit.default_timer()
# 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [10001] * (m + 1)

# 다이나믹 프로그래밍(Dynamic Programming) 진행(보텀업)
d[0] = 0
count = 0
for i in range(n):
    for j in range(array[i], m + 1):
        count += 1
        if d[j - array[i]] != 10001: # (i - k)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j - array[i]] + 1)
end = timeit.default_timer()
# 계산된 결과 출력
print("count=",count) # count= 99903
if d[m] == 10001: # 최종적으로 M원을 만드는 방법이 없는 경우
    print(-1)
else:
    print(d[m])
print("min len 측정     %f초 걸렸습니다." % (end - start))
"""

"""
10 9999
2
3
5
7
9
11
13
14
16
17
"""