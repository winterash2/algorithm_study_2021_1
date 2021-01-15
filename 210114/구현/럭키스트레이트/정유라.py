point = input()
total = 0

for idx in range(len(point)):
    # 자릿수가 절반 넘어가는 순간 total을 음수로 바꾼다
    # 나머지 자릿수를 다 더해서 0이면 왼쪽부분 == 오른쪽 부분
    if idx == len(point) // 2:
        total = -total
    total += int(point[idx])
if total == 0:
    print("LUCKEY")
else:
    print("READY")