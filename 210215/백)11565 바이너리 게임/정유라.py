# 난 정말 당황스러워.
a = input()
b = input()

a_count_1 = a.count("1")
b_count_1 = b.count("1")

if a_count_1 >= b_count_1:
    print("VICTORY")
else:
    if a_count_1 % 2 == 1 and (b_count_1 - a_count_1) == 1:
        print("VICTORY")
    else:
        print("DEFEAT")

# from collections import deque

# a = input()
# b = input()
# q_a = deque(a)
# q_b = deque(b)
# i = 0
# j = 0

# while True:
#     # 다 팝 된 경우
#     if len(q_a)==0 or len(q_a) <= i:
#         break
#     # 첫 번째 자리부터 틀리면 pop
#     if q_a[0] != q_b[0]:
#         q_a.popleft()
#         i = 0
#         continue
#     # 중간에 틀린게 나오면
#     if q_a[i] != q_b[j]:
#         for k in range(0, i):
#             q_a.popleft()
#         i, j = -1, -1 
#     i += 1
#     j += 1

# flag = True
# range_parity = len(q_b) - len(q_a)
# for i in range(range_parity):
#     if q_a.count("1") % 2 == 0:
#         q_a.append("0")
#     else:
#         q_a.append("1")
#     if q_a == q_b:
#         print("VICTORY")
#         flag = False
#         break

# if flag:
#     print("DEFEAT")