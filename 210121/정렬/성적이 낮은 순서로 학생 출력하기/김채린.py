import sys
import operator
input = sys.stdin.readline

# 학생 수
N=int(input())

arr=dict()

for i in range(N):
    M=input().split()
    arr[M[0]]=int(M[1])

sorted_arr=sorted(arr.items(), key=operator.itemgetter(1))

# print(sorted_arr, type(sorted_arr))

for a in sorted_arr:
    print(a[0],end=' ')