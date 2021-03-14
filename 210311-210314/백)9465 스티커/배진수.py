import sys
input = sys.stdin.readline

testcase = int(input())


for _ in range(testcase):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]
    answer = 0
    for i in range(n):
        if i - 2 >= 0:
            arr[0][i] += max(arr[1][i-1], arr[1][i-2])
            arr[1][i] += max(arr[0][i-1], arr[0][i-2])
        elif i - 1 >= 0:
            arr[0][i] += arr[1][i-1]
            arr[1][i] += arr[0][i-1]
    
    print(max(arr[0][-1], arr[1][-1]))