n, m = map(int, input().split())
small_num_list = []
for i in range(n):
    data = list(map(int, input().split()))
    data.sort()
    small_num_list.append(data[0])

small_num_list.sort()
print(small_num_list[n-1])
