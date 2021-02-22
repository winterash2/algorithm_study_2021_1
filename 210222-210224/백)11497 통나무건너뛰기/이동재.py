T = int(input())
for _ in range(T):
    N = int(input())
    trees = list(map(int, input().split()))
    trees.sort()
    left = right = trees[0]
    answer = 0
    for cur in trees[1:]:
        if (cur - left) < (cur - right):
            answer = max(answer, cur - right)
            right = cur
        else:
            answer = max(answer, cur - left)
            left = cur
    answer = max(answer, abs(left - right))
    print(answer)

"""
3
7
13 10 12 11 10 11 12
5
2 4 5 7 9
8
6 6 6 6 6 6 6 6
"""