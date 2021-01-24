import sys
input = sys.stdin.readline

N, K= map(int,input().split())
f_arr=list(map(int,input().split()))
s_arr=list(map(int,input().split()))

f_arr.sort()
s_arr.sort(reverse=True)


# f_arr[0:K]=s_arr[0:K]

for i in range(K):
    if f_arr[i]<s_arr[i]:
        f_arr[i], s_arr[i]=s_arr[i], f_arr[i]
    else:
        break

print(sum(f_arr))