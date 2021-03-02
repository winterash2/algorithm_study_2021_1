# 2차 시도
# [1, 2, 2, 1, 3, 3, 4, 5, 2, 1]
# [1, 5, 2, 1, 4, 3, 3, 3, 2, 1]
# [2, 7, 4, 2, 7, 6, 7, 8, 4, 2]
# 앞으로 한 번, 뒤로 한 번 한 다음에 그 두개를 더한 뒤
# 최대값에서 -1 하면 된다고 해서 그렇게 해봄
# -1 해야하는 이유는 같은 요소가 두 번 들어가기 때문
# 틀린줄 알았는데 성공한거였음, 25번째 줄에서 실수했던거임
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
            dp.append(idx + 1) # 여기서 idx + 1 말고 그냥 idx로 하면 당연히 틀림
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
