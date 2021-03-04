# https://www.acmicpc.net/problem/1697
from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    q=deque()
    q.append(n)

    while q:
        x=q.popleft()
        if x==k:
            print(arr[x])
            break
        for z in (x-1,x+1,x*2): #4 6 10
            if 0 <= z <=m and not arr[z]:
                arr[z]=arr[x]+1
                q.append(z)

m= 100000
arr=[0] * (m+1)
n, k=map(int,input().split())

bfs()