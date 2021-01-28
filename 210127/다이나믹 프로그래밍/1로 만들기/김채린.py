import sys
input = sys.stdin.readline
 
X=int(input())

d = [0 for _ in range(X + 1)]

for i in range(1, X + 1):

    if i == 1:
        d[i] = 0
        continue

    d[i] = d[i-1] + 1

    if i % 5 == 0 and d[i//5] + 1 < d[i]:
        d[i] = d[i//5] + 1

    if i % 3 == 0 and d[i//5] + 1 < d[i]:
        d[i] = d[i//3] + 1
        
    if i % 2 == 0 and d[i//2] + 1< d[i]:
        d[i] = d[i//2] + 1
        
print(d[X])