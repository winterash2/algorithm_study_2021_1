import sys
input = sys.stdin.readline



def fixed_spot(arr, start, end):
    print(arr,start,end)
    while start<=end:
        mid=(end+start)//2

        if mid==arr[mid]:
            # print('A: ',start,mid,end)
            return mid
        elif arr[mid]>mid:
            # print('B: ',start,mid,end)
            end=mid-1
        else:
            # print('C: ',start,mid,end)
            start=mid+1
        
    return -1

a=int(input())
list_a=list(map(int,input().split()))


print(fixed_spot(list_a, 0, a-1))