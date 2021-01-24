import sys
input = sys.stdin.readline

# 수열에 속해있는 수의 개수 N
N=int(input())
arr=[]

for i in range(N):
    arr.append(int(input()))

arr.sort(reverse=True)

for a in arr:
    print(a, end=' ')