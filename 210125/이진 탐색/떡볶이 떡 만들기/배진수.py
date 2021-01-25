n, m = map(int, input().split())
dduck = list(map(int, input().split()))

def make(dduck, mid):
    result = 0
    for dd in dduck:
        if dd > mid:
            result += (dd - mid)
        else:
            continue
    return result


def check(target, dduck, start, end):
    while start <= end:
        mid = (start + end) // 2
        res = make(dduck, mid)
        if target == res:
            return mid
        elif target < res:
            start = mid + 1
        else:
            end = mid - 1
    return False



dduck.sort()
result = check(m, dduck, 0, dduck[-1])
print(result)
