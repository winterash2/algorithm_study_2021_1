import sys
input = sys.stdin.readline

n, x=map(int,input().split())
list_n=list(map(int,input().split()))


# 문제 제대로 안읽은 나의 첫번째 방법...시간복잡도..O(n) 어쩐지 뭐지 싶더라..
# count_x=list_n.count(x)

# if count_x==0:
#     print(-1)
# else:
#     print(count_x)


#두번째
def start_index(arr,target, start, end):

    while start<=end:
        mid=(end+start)//2
        if (mid==0 or target>arr[mid-1])and arr[mid]==target:
            return mid
        elif arr[mid]>=target:
            end=mid-1
        else:
            start=mid+1
    return -1

def end_index(arr,target, start, end):

    while start<=end:
        mid=(end+start)//2
        if (mid==n-1 or target<arr[mid+1])and arr[mid]==target:
            return mid
        elif arr[mid]>target:
            end=mid-1
        else:
            start=mid+1

    return -1

s_idx=start_index(list_n,x,0,n-1)
e_idx=end_index(list_n,x,0,n-1)

if s_idx==-1:
    print(-1)
else:
    print(e_idx-s_idx+1)