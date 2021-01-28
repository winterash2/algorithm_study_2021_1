import sys
input = sys.stdin.readline

n=int(input())
k=list(map(int,input().split()))

d=[0 for _ in range(n)]

d[0]=k[0]
d[1]=max(k[0],k[1])

for i in range(2,n):
    print((d[i-1],d[i-2]+k[i]))
    d[i]=max(d[i-1],d[i-2]+k[i])

print(d)

print(d[n-1])