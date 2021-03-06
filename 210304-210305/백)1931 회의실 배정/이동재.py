import sys
input = sys.stdin.readline

N = int(input())
meetings = []
for _ in range(N):
    start, end = map(int, input().split())
    meetings.append((start, end))

meetings.sort(key = lambda x: (x[1], x[0]))

answer = 0
cur = 0
for start, end in meetings:
    if start >= cur:
        cur = end
        answer += 1

print(answer)