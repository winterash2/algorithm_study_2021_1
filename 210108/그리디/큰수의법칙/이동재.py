n, m, k = [int(x) for x in input().split()]
list_num = [int(x) for x in input().split()]

list_num.sort()

result = (list_num[-1] * k + list_num[-2]) * \
    (m // (k+1)) + (list_num[-1] * (m % (k+1)))
print(result)
