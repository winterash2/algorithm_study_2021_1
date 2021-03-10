# http://boj.kr/1931

# 끝나는 시간을 기준으로 정렬
# 끝나는 시간이 같은 경우 시작시간이 빠른것

n = int(input())
arr = []
for _ in range(n):
    start, end = map(int, input().split())
    arr.append((start, end))

arr.sort(key=lambda x: (x[1], x[0]))
# print(arr)
cnt = 1
# [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
# s, e = arr[0]
e = 0
for i in range(1, n):
    s_t, e_t = arr[i]
    print(">", s_t, e_t)
    if e < s_t:
        cnt += 1
        s, e = s_t, e_t
print(cnt)
    
