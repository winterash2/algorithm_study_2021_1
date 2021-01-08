n,k=map(int,input().split())

count=0
result= n%k
n=n-n%k
while n!=1:
    n=n/k
    count+=1
result+=count
print(result)