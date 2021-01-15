n = int(input())

# 인덱스로 나눠서 확인하기 위해 int -> string
n = str(n)
front_sum = 0
back_sum = 0
for i in range(len(n)):
    if i < len(n)/2:
        front_sum += int(n[i])
    else:
        back_sum += int(n[i])

if front_sum == back_sum:
    print("LUCKY")
else:
    print("READY")