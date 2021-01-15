"""
input_str = input()

right_sum = 0
for input_num in input_str:
    print(input_num)
    right_sum += int(input_num)

left_sum = 0
lucky = False
for input_num in input_str:
    left_sum += int(input_num)
    right_sum -= int(input_num)
    # print("left_sum=", left_sum, "right_sum=", right_sum)
    if left_sum == right_sum:
        lucky = True
        break

if lucky:
    print("LUCKY")
else:
    print("READY")
"""

input_str = input()
left_str = input_str[:(len(input_str) // 2)]
right_str = input_str[(len(input_str) // 2):]

left_sum = 0
right_sum = 0

for l in left_str:
    left_sum += int(l)
for r in right_str:
    right_sum += int(r)

if left_sum == right_sum:
    print("LUCKY")
else:
    print("READY")