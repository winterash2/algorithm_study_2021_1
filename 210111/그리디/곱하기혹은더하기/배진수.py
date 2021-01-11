s = input()

result = 0
for text in s:
    if result * int(text) == 0:
        result += int(text)
    else:
        result *= int(text)

print(result)