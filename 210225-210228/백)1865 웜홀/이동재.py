# 플로이드 워셜 썼음
# 72퍼에서 틀림
import sys
input = sys.stdin.readline

TC = int(input())
for _ in range(TC):
    N, M, W = map(int, input().split())

    INF = float('inf')
    floyd = [[INF for _ in range(N+1)] for _ in range(N+1)]
    for _ in range(M):
        S, E, T = map(int, input().split())
        floyd[S][E] = T
        floyd[E][S] = T
    for _ in range(W):
        S, E, T = map(int, input().split())
        floyd[S][E] = -T
    
    # print("-"*20)
    # [print(floyd[i]) for i in range(len(floyd))]

    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                floyd[i][j] = min(floyd[i][j], floyd[i][k] + floyd[k][j])
    
    enable = False
    for i in range(1, N+1):
        if floyd[i][i] < 0:
            enable = True
            break
    if enable:
        print("YES")
    else:
        print("NO")
