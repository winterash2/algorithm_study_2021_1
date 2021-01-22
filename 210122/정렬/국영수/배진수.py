n = int(input())

record = []
for _ in range(n):
    name, ko_score, en_score, ma_score = map(str, input().split())
    re_list = [name, int(ko_score), int(en_score), int(ma_score)]
    record.append(re_list)

record.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for re in record:
    print(re[0])