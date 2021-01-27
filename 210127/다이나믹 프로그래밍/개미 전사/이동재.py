N = int(input())
warehouses = list(map(int, input().split()))

warehouses[1] = max(warehouses[0], warehouses[1])
for i in range(2, N):
    warehouses[i] = max(warehouses[i-2]+warehouses[i], warehouses[i-1])
    # print(warehouses)

print(max(warehouses[N-1], warehouses[N-2]))