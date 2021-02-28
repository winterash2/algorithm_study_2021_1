import sys
input = sys.stdin.readline

n, k = map(int, input().split())
S = input().rstrip()
list_s = list(S)
cnt = 0
for i in range(len(list_s)):
    if list_s[i] == "P":
        for j in range(i-k, i+k+1):
            if 0 <= j < n and list_s[j] == "H":
                cnt += 1
                list_s[j] = "-"
                break

print(cnt)
# print(list_s)
