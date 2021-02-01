list_2 = [2]
list_3 = [3]
list_5 = [5]

for i in range(900):
    list_2.append(list_2[0]*(i+2))
    list_3.append(list_3[0]*(i+2))
    list_5.append(list_5[0]*(i+2))

res = [1]
res = res + list_2 + list_3 + list_5
res.sort()
result = set(res)
a = list(result)

n = int(input())
print(a[n-1])
