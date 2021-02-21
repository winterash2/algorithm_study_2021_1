# 의외로 되게 쉬운 문제임
# 다만 python에서는 입력이 제대로 안 되고 에러가 계속 나는게 테스트셋이 이상하거나 뭔가 이상한 듯
# pypy3에서도 그냥 input=sys.stdin.readline 이거만 하면 에러남
# 아래와 같이 sys.stdin.readline().rstrip() 이거처럼 rstrip도 해줘야 함

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

"""
동재형이라서 생각보다 쉬웠던 문제..
역시 후덜덜합니다