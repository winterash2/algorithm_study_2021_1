import bisect
import sys
input = sys.stdin.readline

x = int(input())
data = list(map(int, input().split()))

dp = []
dp.append(data[0])
max_data = max(data)


def small(arr, start, end):
    for i in range(start, end):
        if data[i] < arr[-1]:
            arr.append(data[i])
        else:
            index = bisect.bisect_left(arr[start:], data[i])
            arr[index] = data[i]


for i in range(x):
    if dp[-1] == max_data and max_data not in data[i+1:]:
        small(dp, i, x)
        break
    if data[i] > dp[-1]:
        dp.append(data[i])
    else:
        index = bisect.bisect_left(dp, data[i])
        dp[index] = data[i]

dp_small = []
dp_small.append(data[0])
for i in range(x):
    if data[i] < dp_small[-1]:
        dp_small.append(data[i])
    else:
        index = bisect.bisect_left(dp_small, data[i])
        dp_small[index-1] = data[i]


print(len(dp_small))
print(dp_small)
print(len(dp))
