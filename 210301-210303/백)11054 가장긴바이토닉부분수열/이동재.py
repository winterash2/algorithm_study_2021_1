# 2차 시도
# [0, 2, 1, 0, 3, 2, 4, 5, 1, 0]
# [0, 5, 1, 0, 4, 2, 2, 3, 2, 0]
# [0, 7, 2, 0, 7, 4, 6, 8, 3, 0]
# 앞으로 한 번, 뒤로 한 번 한 다음에 그 두개를 더한 뒤
# 최대값에서 -1 하면 된다고 해서 그렇게 해봄
# -1 해야하는 이유는 같은 요소가 두 번 들어가기 때문
# 근데 이것도 실패함
import bisect

N = int(input())
arr = list(map(int, input().split()))


def get_bitonic_dp(arr):
    dp = []
    result = arr[:1]
    for elem in arr:
        if elem > result[-1]:
            result.append(elem)
            dp.append(len(result))
        else:
            idx = bisect.bisect_left(result, elem)
            result[idx] = elem
            dp.append(idx)
    return dp


dp = []
dpPre = get_bitonic_dp(arr)
dpSuf = get_bitonic_dp(arr[::-1])[::-1]
for i in range(len(arr)):
    dp.append(dpPre[i] + dpSuf[i])
print(max(dp) - 1)

# 1차 시도
# 앞에서부터 1개, 2개, ... , n개로 자른 거랑 반대꺼랑 바이토닉 수열 구해서 붙여서 확인
# 실패함
"""
import bisect

N = int(input())
arr = list(map(int, input().split()))


def get_bitonic(arr):
    result = arr[:1]
    for elem in arr:
        if elem > result[-1]:
            result.append(elem)
        else:
            idx = bisect.bisect_left(result, elem)
            result[idx] = elem
    return result


answer = 0
for i in range(N+1):
    arrPre = arr[:i]
    arrSuf = arr[i:]
    arrSuf = arrSuf[::-1]
    curBitonic = get_bitonic(arrPre) + get_bitonic(arrSuf)[::-1]
    answer = max(answer, len(curBitonic))
print(answer)
"""
