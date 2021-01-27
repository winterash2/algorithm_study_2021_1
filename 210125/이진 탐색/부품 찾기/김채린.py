n=5
arr_n=[8,3,7,9,2]
m=3
arr_m=[5,7,9]


arr_n=sorted(arr_n)
print(arr_n)

def binary(arr, target, start, end):
    while start<=end:
        mid=(start+end)//2
        
        if arr[mid]==target:
            return mid
        elif arr[mid]>target:
            end=mid-1
        else:
            start=mid+1
    return None

for i in arr_m:
    answer=binary(arr_n,i, 0, n-1)
    if answer!=None:
        print('yes',end=' ')
    else:
        print('no', end=' ')