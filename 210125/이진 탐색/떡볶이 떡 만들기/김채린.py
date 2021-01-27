import sys
input = sys.stdin.readline

N, M=map(int,input().split())
height=list(map(int,input().split()))

def binary(arr, target, start, end):
    while start<=end:
        new_arr=[0]*N
        mid=(start+end)//2

        for i in range(len(arr)-1):
            x=arr[i]-mid
            if x<0:
                new_arr[i]=0
            else:
                new_arr[i]=x

        if sum(new_arr)==target:
            return mid
        elif sum(new_arr)<target:
            end=mid-1
        else:
            start=mid+1
    return None

answer=binary(height,M, 0,  max(height))

print(answer)


