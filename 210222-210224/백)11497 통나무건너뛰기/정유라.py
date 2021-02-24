# http://boj.kr/11497

for _ in range(int(input())):
    n = int(input())
    trees = list(map(int, input().split()))
    trees.sort()
    tmp = [0] * (len(trees))
    tmp[0] = trees[0]
    length = len(trees)

    idx = 1
    for i in range(1, len(trees)):
        if i % 2 == 1:
            tmp[idx] = trees[i]
            idx += 1
        else:
            tmp[-idx+1] = trees[i]

    diff = -1e9
    for i in range(length-1, -1, -1):
        cha = abs(tmp[i] - tmp[i-1])  
        if diff < cha:
            diff = cha
    print(diff)