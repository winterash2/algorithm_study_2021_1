# https://www.acmicpc.net/problem/11404
import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
INF = float('inf')
floyd = [[INF for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
    a,b,c = map(int, input().split())
    floyd[a][b] = min(floyd[a][b], c) # 아니 같은 곳 가는 버스가 중복해서 있으면 어쩌자는거임...
for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j:
            floyd[i][j] = 0

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            floyd[i][j] = min(floyd[i][j], floyd[i][k] + floyd[k][j])

for i in range(1, N+1):
    for j in range(1, N+1):
        print(floyd[i][j] if floyd[i][j] != INF else 0, end=" ")
    print()

for i in range(1, N+1):
    print(*floyd[i][1:])

"""
5
14 
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
3 5 10
3 1 8
1 4 2
5 1 7
3 4 2
5 2 4
"""