N, K = map(int, input().split())
orders = list(map(int, input().split()))
using = [0 for _ in range(N)]
ordersLen = len(orders)

answer = 0
for i in range(ordersLen):
    cur = orders[i]
    if cur in using:
        pass
    elif 0 in using:
        using[using.index(0)] = cur
    else:
        answer += 1
        removeElem = [x for x in using]
        for j in range(i+1, ordersLen):
            if len(removeElem) <= 1:
                break
            if orders[j] in removeElem:
                removeElem.remove(orders[j])
        using.remove(removeElem[0])
        using.append(cur)

print(answer)


"""
2 7
2 3 2 3 1 2 7
"""


"""
# N, K = map(int, input().split())
# orders = list(map(int, input().split()))
"""
# 원래 이렇게 했었는데 이렇게 하면 문제가 있음
# 맨 앞에 몇개를 미리 집어넣는건데 중복된게 있어도 그냥 둘 다 들어가버려서 틀림
# using = orders[:N]
# orders = orders[N:]
"""
# ordersLen = len(orders)

# answer = 0
# for i in range(ordersLen):
#     cur = orders[i]
#     if cur in using:
#         pass
#     else:
#         answer += 1
#         removeElem = [x for x in using]
#         for j in range(i+1, ordersLen):
#             if len(removeElem) <= 1:
#                 break
#             if orders[j] in removeElem:
#                 removeElem.remove(orders[j])
#         using.remove(removeElem[0])
#         using.append(cur)

# print(answer)
"""
