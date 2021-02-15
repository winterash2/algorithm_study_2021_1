a = input()
b = input()

# n = len(a) * 2
# answer = 'DEFEAT'
# while n >= 0:
#     if  a == b:
#         answer = 'VICTORY'
#         break
#     if len(a) > len(b):
#         a = a[1:]

#     elif len(a) == len(b):
#         a = a[1:]
#     else:
#         temp = 2
#         for i in range(len(a)):
#             if a[i] == '1':
#                 temp += 1
#         if temp % 2 == 0:
#             a += '0'
#         else:
#             a += '1'
#     n -= 1

# print(answer)

a_1 = a.count('1')
b_1 = b.count('1')

if a_1 >= b_1:
    print("VICTORY")
elif a_1 < b_1:
    if (a_1 + 2) % 2 == 1 and (a_1+1) == b_1:
        print("VICTORY")
    else:
        print("DEFEAT")

"""
문제가 매우 맘에 안들었던 문제..ㅎㅎㅎ
a 랑 b가 1의 개수가 같거나 a가 많으면 가능
b가 더 많을 경우에는
b가 a보다 1개만 더 많았을 때, 그것도 1을 추가할수 있는 경우만 가능
"""