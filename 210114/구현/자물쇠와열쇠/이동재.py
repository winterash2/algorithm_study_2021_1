import copy


def rotate_90(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]
    # 왜 'ret = [[0] * N] * N'과 같이 하지 않는지 헷갈리시면 연락주세요.

    for r in range(N):
        for c in range(N):
            ret[c][N-1-r] = m[r][c]
    return ret


def verify(lock_extension_org, key, x, y, M, N):
    lock_extension = copy.deepcopy(lock_extension_org)
    for i in range(M):
        for j in range(M):
            lock_extension[x+i][y+j] += key[i][j]

    # 배열 형태로 출력하는 테스트 코드
    # for x in lock_extension:
    #     for y in x:
    #         print(y, ",", end="")
    #     print()
    # print()

    answer = True
    for i in range(M-1, M-1+N, 1):
        for j in range(M-1, M-1+N, 1):
            if lock_extension[i][j] != 1:
                answer = False
                break
        if answer == False:
            break
    return answer


def solution(key, lock):
    M = len(key)
    N = len(lock)

    # 자물쇠 배열에 M-1 크기로 패딩을 추가해줌
    lock_extension = []
    for _ in range(M-1):
        blank = [0 for _ in range(((M-1)*2)+N)]
        lock_extension.append(blank)
    for l in lock:
        blank = [0 for _ in range(M-1)]
        blank += l
        blank += [0 for _ in range(M-1)]
        lock_extension.append(blank)
    for _ in range(M-1):
        blank = [0 for _ in range(((M-1)*2)+N)]
        lock_extension.append(blank)

    # 원래 key로 검증
    answer = False
    for x in range(M-1+N):
        for y in range(M-1+N):
            answer = verify(lock_extension, key, x, y, M, N)
            if answer:
                return answer

    # 90도 돌린 key로 검증
    key = rotate_90(key)
    answer = False
    for x in range(M-1+N):
        for y in range(M-1+N):
            answer = verify(lock_extension, key, x, y, M, N)
            if answer:
                return answer

    # 180도 돌린 key로 검증
    key = rotate_90(key)
    answer = False
    for x in range(M-1+N):
        for y in range(M-1+N):
            answer = verify(lock_extension, key, x, y, M, N)
            if answer:
                return answer

    # 270도 돌린 key로 검증
    key = rotate_90(key)
    answer = False
    for x in range(M-1+N):
        for y in range(M-1+N):
            answer = verify(lock_extension, key, x, y, M, N)
            if answer:
                return answer

    return answer


key = [  # M * M
    [0, 0, 0],
    [1, 0, 0],
    [0, 1, 1]
]
lock = [  # N * N
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1]
]
print(solution(key, lock))

# 시간은 좀 오래 걸리지만 통과, 효율성 검사는 없어서 100점
# 테스트 1 〉	통과 (2.98ms, 10.3MB)
# 테스트 2 〉	통과 (0.79ms, 10.3MB)
# 테스트 3 〉	통과 (204.55ms, 10.4MB)
# 테스트 4 〉	통과 (0.19ms, 10.4MB)
# 테스트 5 〉	통과 (352.17ms, 10.4MB)
# 테스트 6 〉	통과 (328.18ms, 10.4MB)
# 테스트 7 〉	통과 (371.41ms, 10.3MB)
# 테스트 8 〉	통과 (1318.53ms, 10.4MB)
# 테스트 9 〉	통과 (1557.72ms, 10.4MB)
# 테스트 10 〉	통과 (4148.79ms, 10.3MB)
# 테스트 11 〉	통과 (4776.93ms, 10.4MB)
# 테스트 12 〉	통과 (0.10ms, 10.4MB)
# 테스트 13 〉	통과 (102.26ms, 10.4MB)
# 테스트 14 〉	통과 (22.66ms, 10.4MB)
# 테스트 15 〉	통과 (51.82ms, 10.4MB)
# 테스트 16 〉	통과 (451.40ms, 10.3MB)
# 테스트 17 〉	통과 (17.44ms, 10.4MB)
# 테스트 18 〉	통과 (436.54ms, 10.3MB)
# 테스트 19 〉	통과 (6.58ms, 10.3MB)
# 테스트 20 〉	통과 (1712.88ms, 10.3MB)
# 테스트 21 〉	통과 (209.99ms, 10.3MB)
# 테스트 22 〉	통과 (397.87ms, 10.3MB)
# 테스트 23 〉	통과 (36.98ms, 10.4MB)
# 테스트 24 〉	통과 (35.53ms, 10.3MB)
# 테스트 25 〉	통과 (1780.30ms, 10.4MB)
# 테스트 26 〉	통과 (2967.27ms, 10.4MB)
# 테스트 27 〉	통과 (5249.98ms, 10.4MB)
# 테스트 28 〉	통과 (298.02ms, 10.3MB)
# 테스트 29 〉	통과 (67.67ms, 10.3MB)
# 테스트 30 〉	통과 (457.08ms, 10.4MB)
# 테스트 31 〉	통과 (1007.52ms, 10.4MB)
# 테스트 32 〉	통과 (2745.53ms, 10.5MB)
# 테스트 33 〉	통과 (460.84ms, 10.2MB)
# 테스트 34 〉	통과 (1.96ms, 10.3MB)
# 테스트 35 〉	통과 (22.81ms, 10.4MB)
# 테스트 36 〉	통과 (45.55ms, 10.3MB)
# 테스트 37 〉	통과 (32.33ms, 10.3MB)
# 테스트 38 〉	통과 (7.33ms, 10.3MB)
