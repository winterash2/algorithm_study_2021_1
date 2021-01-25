import sys
input = sys.stdin.readline

n = int(input())
have = list(map(int, input().split()))

m = int(input())
needs = list(map(int, input().split()))


def check(val, have, start, end):
    while start <= end:
        mid = (start + end) // 2
        if have[mid] == val:
            return True
        elif val < have[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return False


have.sort()
for need in needs:
    if check(need, have, 0, len(have)):
        print("yes")
    else:
        print("no")
