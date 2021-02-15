from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    print("----------------------input-----------------------")
    N = int(input())
    last_rank = list(map(int, input().split()))
    M = int(input())
    change_rank = []
    for _ in range(M):
        a, b = list(map(int, input().split()))
        change_rank.append((a, b))
    print("----------------------answer----------------------")
    indegrees = [0 for _ in range(N)]
    
    graph = [[False for _ in range(N+1)] for _ in range(N+1)]
    for last in last_rank:
        



"""
3
5
5 4 3 2 1
2
2 4
3 4
3
2 3 1
0
4
1 2 3 4
3
1 2
3 4
2 3

"""