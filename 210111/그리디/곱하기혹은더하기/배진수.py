s = input()

result = 0
for text in s:
    if result * int(text) == 0 or result * int(text) == 1 or text == 1:
        result += int(text)
    else:
        result *= int(text)

print(result)