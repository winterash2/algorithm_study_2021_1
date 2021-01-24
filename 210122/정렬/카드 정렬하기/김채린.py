import sys
import heapq
input = sys.stdin.readline

# 카드 묶음 수
N=int(input())

arr=[]

for i in range(N):
    heapq.heappush(arr, int(input()))

result = 0

while len(arr) != 1:
    first = heapq.heappop(arr)
    second = heapq.heappop(arr)
    sum_val=first+second
    result += sum_val
    heapq.heappush(arr, sum_val)

print(result)




# ------------------------------------
# for a in range(N):
#     arr.append(int(input()))

# arr=sorted(arr)

# sum_arr=[]

# while len(arr)!=1:
#     k=arr[0]+arr[1]
#     sum_arr.append(k)
#     arr.pop(0)
#     arr[0]=k
#     print(arr,'     ',sum_arr)


# print(sum(sum_arr))

# 헐 난 바보 왜 안되나 했네..
# [3, 3, 4, 5]       [3]
# [6, 4, 5]       [3, 6]
# [10, 5]       [3, 6, 10]
# [15]       [3, 6, 10, 15]