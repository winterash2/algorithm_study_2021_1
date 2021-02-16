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
"""

# 뻘짓 했는데 결국 안 돌아감...
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
    if goal[idx_goal] == "0" and base[(-idx_goal) + (-1)] == "0":
        idx_goal += 1
    else:
        break

enable = False
while True:
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