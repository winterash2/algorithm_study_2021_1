n = int(input())
# 연산을 수행하고자 하는 수 리스트
data = list(map(int, input().split()))
# 더하기, 빼기, 곱하기, 나누기 연산자 개수
add, sub, mul, div = map(int, input().split())

# 최솟값과 최댓값 초기화
min_value = 1e9
max_value = -1e9

# 깊이 우선 탐색 (DFS) 메서드
def dfs(i, now):
    global min_value, max_value, add, sub, mul, div
    # 모든 연산자를 다 사용한 경우, 최솟값과 최댓값 업데이트
    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else:
        # 각 연산자에 대하여 재귀적으로 수행
        if add > 0:
            add -= 1
            dfs(i + 1, now + data[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i + 1, now - data[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, now * data[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, int(now / data[i])) # 나눌 때는 나머지를 제거
            div += 1

# DFS 메서드 호출
dfs(1, data[0])

# 최댓값과 최솟값 차례대로 출력
print(max_value)
print(min_value)


# 처음에 이렇게 접근했는데 답안을 보니까 너무 간단하고 좋은 코드가 있어서 그걸로 대체함
"""
from itertools import permutations

N = int(input())
numbers = [int(x) for x in input().split()]
add, sub, mul, div = [int(x) for x in input().split()]

# N = 6
# numbers = [1, 2, 3, 4, 5, 6]
# add, sub, mul, div = 2, 1, 1, 1

all_operators = []
for _ in range(add):
    all_operators.append("+")
for _ in range(sub):
    all_operators.append("-")
for _ in range(mul):
    all_operators.append("*")
for _ in range(div):
    all_operators.append("/")

all_operators_permutations = list(set(permutations(all_operators, N-1)))


def calc(numbers, operators):
    result = numbers[0]
    numbers = numbers[1:]
    for i, number in enumerate(numbers):
        if operators[i] == "+":
            result += number
        if operators[i] == "-":
            result -= number
        if operators[i] == "*":
            result *= number
        if operators[i] == "/":
            if result < 0:
                result = abs(result) // number
                result *= -1
            else:
                result = result // number
    return result


min_val = max_val = calc(numbers, all_operators_permutations[0])
all_operators_permutations = all_operators_permutations[1:]
for operators in all_operators_permutations:
    calc_result = calc(numbers, operators)
    if calc_result > max_val:
        max_val = calc_result
    elif calc_result < min_val:
        min_val = calc_result

print(max_val)
print(min_val)
"""