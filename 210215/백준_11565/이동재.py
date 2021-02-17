# 백준 숏코더... 미친 사람...
"""
n=input().count("1")
print(("DEFEAT","VICTORY")[n+n%2>=input().count("1")])
"""

# 갓 진수....
"""
a = input()
b = input()

a_1 = a.count('1')
b_1 = b.count('1')

if a_1 >= b_1:
    print("VICTORY")
elif a_1 < b_1:
    if (a_1 + 2) % 2 == 1 and (a_1+1) == b_1:
        print("VICTORY")
    else:
        print("DEFEAT")
# 문제가 매우 맘에 안들었던 문제..ㅎㅎㅎ
# a 랑 b가 1의 개수가 같거나 a가 많으면 가능
# b가 더 많을 경우에는
# b가 a보다 1개만 더 많았을 때, 그것도 1을 추가할수 있는 경우만 가능
"""


# 0111 -> 000111 되는건 제일 처음 1을 맨 뒤에 가져다 붙이면 되기 때문임
# 따라서 개수가 같으면 무조건 생성 가능
# 앞에 0이 아무리 많이 붙어있어도 상관없음
# 0111
# 01111
# 01111000
#   1110001
#    110001
#     100011
#      000111

# 1110 일 때를 생각해보자
# 11101 로 1을 하나 추가해주면
# 0으로 시작해도 상관없고 1로 시작해도 상관없이 1이 4개 이하인 것들은 전부 만들 수 있음
# 즉 처음 시작할 때 parity가 1인 base는 1이 base.count("1") + 1 인 것까지 만들 수 있음
# 이것을 코드로 옮기면 아래와 같음
base = input()
goal = input()

if base.count('1') + (base.count('1') % 2) >= goal.count('1'):
    print("VICTORY")
else:
    print("DEFEAT")


# 뻘짓 했는데 결국 안 돌아감...
# 0001, 0001 이런거 걸러내지 못 함
"""
base = input()
goal = input()
# base = "01011"
# goal = "1110"

parityA = base.count('1') % 2
parityA = str(parityA)

idx_base = 0
idx_goal = 0
while True:
    if idx_goal >= len(goal) or idx_goal >= len(base):
        break
    if goal[idx_goal] == "0" and base[(-idx_goal) + (-1)] == "0":
        idx_goal += 1
    else:
        break

enable = False
while True:
    print(idx_base, idx_goal)
    # print("parityA=",parityA)
    if idx_base >= len(base):
        break
    if idx_goal >= len(goal):
        enable = True
        break
    
    if parityA == goal[idx_goal]:
        if parityA == "1":
            parityA = "0"
        idx_goal += 1
    else:
        if base[idx_base] == "1":
            parityA = "0" if parityA == "1" else "1"
        idx_base += 1

if enable:
    print("VICTORY")
else:
    print("DEFEAT")
"""