# 아래부터 채워나가면 어떨까 싶어서 해봤는데 시간 오래 걸림
# 이게 1000이면 책 코드가 600이고 아래 백준에서 가져온건 60임
# 책 코드도 아래부터 올라가네... 난 아주 비효율적이게 풀었어...
X = int(input())
dp_table = [1e9] * (X+1)
dp_table[1] = 0
for i in range(1, X, 1):
    # print(dp_table)
    if i+1 <= X:
        dp_table[i+1] = min(dp_table[i+1], dp_table[i]+1)
    if i*2 <= X:
        dp_table[i*2] = min(dp_table[i*2], dp_table[i]+1)
    if i*3 <= X:
        dp_table[i*3] = min(dp_table[i*3], dp_table[i]+1)
    if i*5 <= X:
        dp_table[i*5] = min(dp_table[i*5], dp_table[i]+1)
# print(dp_table)
print(dp_table[X])

# 유라꺼 32000 입력하면 IndexError: list assignment index out of range 에러 뜸


# 백준에서 찾은 훨씬 빠른 예시
# dict를 이용해서 훨씬 빠르게 품
# dp
def dp(n):
    if n in memo:
        return memo[n]
    # 나머지를 더해준 이유 짐작: 7의 경우 2, 3으로 나누어 지지 않으므로 -1를 무조건 해줘야한다.
    # 이 경우를 나머지로 더해주는 것으로 짐작된다.
    m = 1 + min(dp(n // 2) + n % 2, dp(n // 3) + n % 3)
    memo[n] = m
    return m
memo = {1: 0, 2: 1}
n = int(input())
print(dp(n))