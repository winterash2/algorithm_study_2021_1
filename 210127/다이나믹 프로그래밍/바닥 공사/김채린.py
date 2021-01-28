N = int(input())
d = [0 for _ in range(n)]

d[0] = 1
d[1] = 3
for i in range(2, N):
    d[i] = (d[i-1]+2*d[i-2]) % 796796
print(d[N-1])
