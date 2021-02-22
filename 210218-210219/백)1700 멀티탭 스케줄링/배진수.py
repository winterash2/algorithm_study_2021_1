import sys
input = sys.stdin.readline

n, k = map(int, input().split())
multi_tab = [0] * n

uses = list(map(int, input().split()))
res = 0

for i in range(k):
    # print(multi_tab)
    if uses[i] in multi_tab:
        continue
    elif 0 in multi_tab:
        index = multi_tab.index(0)
        multi_tab[index] = uses[i]
    else:
        temp = 0
        cnt = 0
        for multi in multi_tab:
            if multi not in uses[i:]:
                temp = multi
                break
            elif uses[i:].index(multi) > cnt:
                cnt = uses[i:].index(multi)
                temp = multi
        multi_tab[multi_tab.index(temp)] = uses[i]
        res += 1

print(res)
