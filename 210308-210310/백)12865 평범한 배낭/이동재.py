# 81퍼에서 틀렸었는데 그 이유는 22번째 줄에서 maxValue 대신 maxValue-1 로 했었어서임
# 약 2700ms
import sys
input = sys.stdin.readline

N, K = map(int, input().split())  # N(1 ≤ N ≤ 100), K(1 ≤ K ≤ 100,000)
items = []
maxValue = 0
for _ in range(N):
    w, v = map(int, input().split())  # W(1 ≤ W ≤ 100,000), V(0 ≤ V ≤ 1,000)
    maxValue += v
    items.append((w, v))

INF = float('inf')
dp = [INF for _ in range(maxValue+1)]
for w, v in items:
    for idx in range(maxValue-1, -1, -1):
        if dp[idx] != INF:
            dp[idx+v] = min(dp[idx+v], dp[idx] + w)
    dp[v] = min(dp[v], w)

# print(dp)
answer = 0
for value in range(maxValue, -1, -1):
    if dp[value] <= K:
        answer = value
        break

print(answer)


# 백준 모범답안, dict 이용, 588ms
# import sys
read = sys.stdin.readline


def solve():
    N, max_weight = map(int, read().split())
    dp = {0: 0}

    for _ in range(N):
        w, v = map(int, read().split())
        tmp = {}
        for prev_w, prev_v in dp.items():
            if prev_w + w <= max_weight and dp.get(prev_w + w, 0) < prev_v + v:
                tmp[prev_w + w] = prev_v + v
        dp.update(tmp)

    print(max(dp.values()))


solve()
