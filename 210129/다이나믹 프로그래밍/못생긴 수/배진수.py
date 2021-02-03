list_2 = [2]
list_3 = [3]
list_5 = [5]

for i in range(900):
    list_2.append(2*(i+2))
    list_3.append(3*(i+2))
    list_5.append(5*(i+2))

res = [1]
res = res + list_2 + list_3 + list_5
res.sort()
result = set(res)
a = list(result)

n = int(input())
# print(a[n-1])
for i in range(n):
    print(list_2[i] ,end=" ")
