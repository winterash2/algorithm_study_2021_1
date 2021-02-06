import sys
input = sys.stdin.readline


def find_gate(docking, x):
    if len(docking[x]) > 1:
        return False
    else:
        return True


G = int(input())
P = int(input())

docking = [[] for _ in range(G + 1)]
count = 0
cnt = 0
for i in range(1, P + 1):
    data = int(input())
    docking[data].append(i)
    res = find_gate(docking, data)
    if res:
        count += 1
        continue
    elif not res:
        cnt = count
print(count)
