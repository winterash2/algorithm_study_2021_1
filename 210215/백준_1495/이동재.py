N, S, M = map(int, input().split())
V = list(map(int, input().split()))

prev_list = [S]
next_list = []

for diff in V:
    for p in prev_list:
        if M >= p - diff >= 0:
            next_list.append(p-diff)
        if M >= p + diff >= 0:
            next_list.append(p+diff)
    next_list = list(set(next_list))
    prev_list = next_list
    next_list = []

answer = -1
for n in prev_list:
    if n > answer:
        answer = n

print(answer)
"""
3 5 10
5 3 7
"""