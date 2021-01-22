import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
scores = []
for _ in range(N):
    name, kor, eng, math = input().split()
    scores.append([int(kor), int(eng), int(math), name])

# N = 12
# scores = [[50, 60, 100, 'Junkyu'], [80, 60, 50, 'Sangkeun'], [80, 70, 100, 'Sunyoung'], [50, 60, 90, 'Soong'], [50, 60, 100, 'Haebin'], [60, 80, 100, 'Kangsoo'], [80, 60, 100, 'Donghyuk'], [70, 70, 70, 'Sei'], [70, 70, 90, 'Wonseob'], [70, 70, 80, 'Sanghyun'], [80, 80, 80, 'nsj'], [50, 60, 90, 'Taewhan']]

scores.sort(key = lambda x : (-x[0], x[1], -x[2], x[3]))

for _, _, _, name in scores:
    print(name)
    print("\n")