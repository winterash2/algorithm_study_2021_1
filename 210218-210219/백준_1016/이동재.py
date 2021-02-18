min, max = map(int, input().split())
dp = [1 for _ in range(max-min+1)]

i = 1
while True:
    i += 1
    for j in range( min//(i*i), (max//(i*i))+1 ):
        if min <= i*i*j <= max:
            dp[i*i*j-min] = 0
    if i*i > max:
        break

# print(dp)
print(sum(dp))