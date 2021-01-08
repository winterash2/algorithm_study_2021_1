n,m,k=map(int,input().split())


a=list(map(int,input().split()))
a.sort(reverse=True)

index=0
big_num=0
i=0
count=0

while index!=m:
    if(count==k):
        big_num+=a[i+1]
        count=0
    else: 
        big_num+=a[i]
        count+=1
    index+=1

print(big_num)