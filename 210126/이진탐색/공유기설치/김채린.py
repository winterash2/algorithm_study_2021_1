import sys
input = sys.stdin.readline
 
N, C = map(int, input().split())
x = sorted([int(input()) for _ in range(N)])

result = 0
left = 0
right = max(x)
 
while left <= right:
    a = mid = (left + right) // 2
 
    if mid * C > max(x):
        right = mid - 1
        continue
    
    count = 1
    val = x[0] + a
    for i in range(1, len(x)):
        if val > x[i]:
            continue
        else:
            val = x[i] + a
            count += 1
    
    if count < C:
        right = mid - 1
    else:
        result = mid
        left = mid + 1
        
print(result)


# 숏코드는 언제봐도 신기해
# from bisect import*
# n,c=map(int,input().split());x=sorted(int(input())for _ in[0]*n)
# l=1;h=10**9
# while l<h:
#  m=l+h>>1;b=c;t=0
#  while t<n and b:b-=1;t=bisect(x,x[t]+m) 
#  if b:h=m
#  else:l=m+1
# print(l)