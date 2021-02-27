import sys
input = sys.stdin.readline

T = input().rstrip()
P = input().rstrip()

index_P = [0] * len(P)

j = 0
for i in range(1, len(P)):
    while j > 0 and P[i] != P[j]:
        j = index_P[j-1]
    if P[i] == P[j]:
        j += 1
        index_P[i] = j


j = 0
find = []
for i in range(len(T)):
    while j > 0 and T[i] != P[j]:
        j = index_P[j - 1]
    if T[i] == P[j]:
        if j == len(P) - 1:
            find.append(i - len(P) + 2)
            j = index_P[j]
        else:
            j += 1

print(len(find))
# print(*find)
print(' '.join(map(str, find)))
