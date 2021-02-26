# http://boj.kr/19941

# 1. p를 만나면 범위 안에서 먹을 수 있는 햄버거 중에 왼쪽. 
# 2. 먹은 햄버거에는 0을 넣자

from collections import deque

n, k = map(int, input().split())
hp = list(input())

# 사람이 있는 자리 
p_idx = []
for i in range(len(hp)):
    if hp[i] == 'P':
        p_idx.append(i)
q_p_idx = deque(p_idx)

answer = 0
while q_p_idx:
    now_p = q_p_idx.popleft()
    # 사람이 있는 자리에서 닿을 수 있는 범위 안에서 햄버거 찾기
    for idx in range(now_p-k, now_p+k+1):
        # 벗어나는 범위 처리
        if idx < 0 or idx >= n:
            continue

        # 찾으면 결과 처리 후 break
        if hp[idx] == 'H':
            answer += 1
            hp[idx] = 0
            break

print(answer)


