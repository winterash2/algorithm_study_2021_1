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