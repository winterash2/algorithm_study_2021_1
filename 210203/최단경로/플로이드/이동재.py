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