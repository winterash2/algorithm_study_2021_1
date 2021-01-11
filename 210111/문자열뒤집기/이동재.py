input_list = [int(x) for x in input()]

base = input_list[0]
prev = base
count = 0

for i in input_list:
    if i == prev:
        continue
    else:
        prev = i
        if i != base:
            count += 1

print(count)
