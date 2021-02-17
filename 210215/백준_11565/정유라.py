from collections import deque

a = input()
b = input()
print(a, b)
q_a = deque(a)
q_b = deque(b)
i = 0
cnt = 0
print(q_a.popleft(), q_a)
while True:
    # 다 팝 된 경우
    if len(q_a)==0:
        break
    # 첫 번째 자리부터 틀리면 pop
    if q_a[0] != q_b[0]:
        q_a.popleft
    
    # 중간에 틀린게 나오면
    if q_a[i] != q_b[i]:
        del q_a[:i-1]
 
    i += 1
print(">>", q_a)