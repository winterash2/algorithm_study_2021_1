n, m = map(int, input().split())
array = []
for _ in range(n):
    array.append(int(input()))

d = [10001] * (m + 1)

d[0] = 0  # d[0] 초기화
for i in array:
    for j in range(i, m + 1):
        # print("--------")
        # print("i:",i,"j:",j)
        d[j] = min(d[j], d[j-i]+1)
        # print("d[j]:", d[j])


if d[m] == 10001:
    print(-1)
else:
    print(d[m-1])