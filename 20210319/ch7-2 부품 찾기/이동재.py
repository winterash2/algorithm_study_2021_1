import bisect
N = int(input())
stocks = list(map(int, input().split()))
stocks.sort()
M = int(input())
orders = list(map(int, input().split()))

possible = True
for order in orders:
    idx = bisect.bisect_left(stocks, order)
    if stocks[idx] == order:
        print("yes", end=' ')
    else:
        print("no", end=' ')

"""
5
8 3 7 9 2
3
5 7 9
"""
"""
6
8 3 7 9 2 5
3
5 7 9
"""