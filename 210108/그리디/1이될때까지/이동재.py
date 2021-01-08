n, k = [int(x) for x in input().split()]

cnt = 0

while(True):
    if n == 1:
        break
    cnt += 1
    if n % k == 0:
        n = n / k
    else:
        n = n-1

print(cnt)