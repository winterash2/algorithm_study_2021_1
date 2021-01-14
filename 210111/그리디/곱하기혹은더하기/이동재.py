input_str = input()
input_list = []

for char in input_str:
    input_list.append(int(char))

result = 0
for i in input_list:
    if result <= 1:
        result += i
    elif i <= 1:
        result += i
    else:
        result *= i

print(result)