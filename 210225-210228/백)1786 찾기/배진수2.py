# 문자열 검색 - 라빈 카프 방법 (시간초과남) O(N+M)
import sys
input = sys.stdin.readline


def find(parent, pattern):
    parent_size = len(parent)
    pattern_size = len(pattern)
    parent_hash = 0
    pattern_hash = 0
    answer = []
    power = 1
    for i in range(parent_size - pattern_size):
        if i == 0:
            for j in range(pattern_size):
                parent_hash += ord(parent[pattern_size - 1 - j]) * power
                pattern_hash += ord(pattern[pattern_size - 1 - j]) * power
                power *= 2
        else:
            parent_hash = 2 * \
                (parent_hash - ord(parent[i-1]) * (power//2)
                 ) + ord(parent[pattern_size - 1 + i])

        if pattern_hash == parent_hash:
            chk = True
            for k in range(pattern_size):
                if parent[k+i] != pattern[k]:
                    chk = False
            if chk:
                answer.append(i+1)
    return answer


T = input().rstrip()
P = input().rstrip()

res = find(T, P)
print(len(res))
print(' '.join(map(str, res)))
