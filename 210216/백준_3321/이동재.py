# from pprint import pprint
# import copy
import sys

N, M = map(int, input().split())
graph = [[] for _ in range(N)]

for i in range(N):
    input_data = sys.stdin.readline().rstrip()
    # print(input_data)
    try:
        graph[i] = [int(i) for i in input_data]
    except:
        print("error")
        print("error")
        print("error")

for i in range(1, N):
    for j in range(M):
        if graph[i][j] == 1:
            graph[i][j] = graph[i-1][j] + 1

max_size = 0
for i in range(N):
    arr = graph[i]
    arr.sort(reverse=True)
    for idx in range(M):
        size = (idx+1) * arr[idx]
        max_size = size if size > max_size else max_size

print(max_size)

"""
10 6
001010
111110
011110
111110
011110
111111
110111
110111
000101
010101
"""