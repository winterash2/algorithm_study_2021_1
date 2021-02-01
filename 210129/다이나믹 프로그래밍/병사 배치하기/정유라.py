n = 7
array = [15, 11, 4, 8, 5, 2, 4]

array.reverse()
dp = [1] * n
for i in range(1, n):
    for j in range(0,i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(n - max(dp))




# n = 7
# array = [15, 11, 4, 8, 5, 2, 4]
# dp = [1] * n
# for i in range(1, n):
#     if array[i] > array[i-1]:
#         continue
#     dp[i] += max(array[i], array[i+1])

# print(max(dp))